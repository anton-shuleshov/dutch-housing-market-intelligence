#!/usr/bin/env python3
"""Reproduce small, analysis-ready CSVs from official CBS StatLine bulk ZIPs.
Works with Python 3 standard library only. No artificial observations are generated.
Raw ZIPs belong in data/raw/cbs; output written to data/processed.
This parser handles CBS long-form Observations.csv + code lookup tables.
"""
from pathlib import Path
import zipfile, csv, io, re, collections, datetime

ROOT = Path(__file__).resolve().parents[1]
RAW, OUT = ROOT / 'data/raw/cbs', ROOT / 'data/processed'
OUT.mkdir(parents=True, exist_ok=True)

ALIASES = {'Utrecht (gemeente)': 'Utrecht'}
SELECT = ['Nederland','Amsterdam','Haarlem','Heemstede','Beverwijk','Heemskerk',
          'Uitgeest','Alkmaar','Velsen','Zandvoort','Bloemendaal','Arnhem','Utrecht']

def table(tid):
    candidates = list(RAW.glob(f'{tid}-*.zip'))
    if len(candidates) != 1:
        raise FileNotFoundError(f'Expected exactly one ZIP for {tid} under {RAW}; found {len(candidates)}')
    return zipfile.ZipFile(candidates[0]), candidates[0].name

def iter_csv(z, member):
    with z.open(member) as f:
        yield from csv.DictReader(io.TextIOWrapper(f, encoding='utf-8-sig', newline=''), delimiter=';')

def lookups(z, member):
    return {r['Identifier']:r for r in iter_csv(z,member)}

def number(v):
    if not v: return None
    try: return float(v.replace('.', '').replace(',', '.')) if ',' in v else float(v)
    except ValueError: return None

def store(filename, fields, rows):
    p=OUT/filename
    with p.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields)
        w.writeheader(); w.writerows(rows)
    print(f'CREATED {p.relative_to(ROOT)} — {len(rows)} rows')
    return len(rows)

def validate_period(periode):
    return int(periode[:4]) if re.fullmatch(r'\d{4}JJ00',periode) else None

# Prices: 83625NED, one official measure (EUR per sold house), annual municipal / NL.
z,src=table('83625NED')
reg=lookups(z,'RegioSCodes.csv'); periods=lookups(z,'PeriodenCodes.csv')
prices=[]
for r in iter_csv(z,'Observations.csv'):
    region=ALIASES.get(reg.get(r['RegioS'],{}).get('Title'), reg.get(r['RegioS'],{}).get('Title'))
    year=validate_period(r['Perioden'])
    v=number(r['Value'])
    if r['Measure']=='M001534' and region in SELECT and year and year>=2015 and v is not None:
        prices.append(dict(year=year,municipality=region,region_code=r['RegioS'],
            average_sale_price_eur=round(v),status=periods[r['Perioden']]['Status'],source_id='83625NED'))
prices.sort(key=lambda x:(x['municipality'],x['year']))
store('cbs_municipal_sale_prices.csv',list(prices[0]),prices)
z.close()

# Household income: population and characteristic must both mean all private households.
# Median disposable income in 1000 euros -> multiply by 1000 to get EUR.
z,src=table('86380NED')
reg=lookups(z,'RegioSCodes.csv'); periods=lookups(z,'PeriodenCodes.csv')
incomes=[]
for r in iter_csv(z,'Observations.csv'):
    if not (r['Measure'] in ('M000933','M000220') and r['Populatie']=='1050010'
            and r['KenmerkenVanHuishoudens']=='1050010'): continue
    region=ALIASES.get(reg.get(r['RegioS'],{}).get('Title'), reg.get(r['RegioS'],{}).get('Title'))
    year=validate_period(r['Perioden']); v=number(r['Value'])
    if region in SELECT and year and year>=2015 and v is not None:
        incomes.append(dict(year=year,municipality=region,region_code=r['RegioS'],
            income_measure='median_disposable' if r['Measure']=='M000933' else 'mean_disposable',
            household_income_eur=round(v*1000),status=periods[r['Perioden']]['Status'],source_id='86380NED'))
incomes.sort(key=lambda x:(x['municipality'],x['year'],x['income_measure']))
store('cbs_municipal_income.csv',list(incomes[0]),incomes)
z.close()

# Explicit comparable ratio: average dwelling SALE price / median annual disposable household income.
# This is NOT official mortgage affordability and never price of a standard home.
med={(r['year'],r['region_code']):r for r in incomes if r['income_measure']=='median_disposable'}
afford=[]
for p in prices:
    m=med.get((p['year'],p['region_code']))
    if m and m['household_income_eur']>0:
        afford.append(dict(year=p['year'],municipality=p['municipality'],region_code=p['region_code'],
            average_sale_price_eur=p['average_sale_price_eur'],
            median_disposable_income_eur=m['household_income_eur'],
            price_to_income_ratio=round(p['average_sale_price_eur']/m['household_income_eur'],3),
            income_status=m['status'],price_status=p['status'],price_source='83625NED',income_source='86380NED'))
afford.sort(key=lambda x:(x['municipality'],x['year']))
store('cbs_price_to_income_ratio.csv',list(afford[0]),afford)

# National price index: monthly series, 2020=100. No mixed quarter/year time scales.
z,src=table('85773NED'); periods=lookups(z,'PeriodenCodes.csv')
index=[]
for r in iter_csv(z,'Observations.csv'):
    per=r['Perioden']
    if r['Measure']!='M001505_2' or not re.fullmatch(r'\d{4}MM\d{2}',per): continue
    v=number(r['Value'])
    if v is not None and int(per[:4])>=2015:
        index.append(dict(year=int(per[:4]),month=int(per[-2:]),year_month=per[:4]+'-'+per[-2:],
            index_2020_100=v,status=periods[per]['Status'],source_id='85773NED'))
index.sort(key=lambda x:x['year_month'])
store('cbs_national_house_price_index_monthly.csv',list(index[0]),index)
z.close()

# National building stock mutations: yearly from 2012 onward (BAG methodologies caveat).
z,src=table('82235NED'); measures=lookups(z,'MeasureCodes.csv'); periods=lookups(z,'PeriodenCodes.csv')
keep={'M003003':'new_construction','D003024':'demolition','D002968':'end_housing_stock_thousands'}
construction=[]
for r in iter_csv(z,'Observations.csv'):
    year=validate_period(r['Perioden']);v=number(r['Value'])
    if r['Measure'] in keep and year and year>=2012 and v is not None:
        construction.append(dict(year=year,metric=keep[r['Measure']],value=v,
            unit=measures[r['Measure']]['Unit'],status=periods[r['Perioden']]['Status'],source_id='82235NED'))
construction.sort(key=lambda x:(x['year'],x['metric']))
store('cbs_national_housing_stock_mutations.csv',list(construction[0]),construction)
z.close()

# Dutch rental increases: national total, not monthly rental euros.
z,src=table('83163NED'); periods=lookups(z,'PeriodenCodes.csv')
rents=[]
for r in iter_csv(z,'Observations.csv'):
    year=validate_period(r['Perioden']);v=number(r['Value'])
    if r['SoortVerhuur']=='T001549' and r['Measure'] in ('D001503','D001504') and year and v is not None:
        rents.append(dict(year=year,measure='incl_harmonisation' if r['Measure']=='D001503' else 'excl_harmonisation',
            rent_increase_pct=v,status=periods[r['Perioden']]['Status'],source_id='83163NED'))
rents.sort(key=lambda x:(x['year'],x['measure']))
store('cbs_national_rent_increase.csv',list(rents[0]),rents)
z.close()

# Municipal permits: only newly permitted residential homes, totals by contractor and owner, quarterly
# aggregated into calendar years. Permits are not completed dwellings.
z,src=table('83671NED');reg=lookups(z,'RegioSCodes.csv'); periods=lookups(z,'PeriodenCodes.csv')
permits=collections.defaultdict(float);status=collections.defaultdict(set)
for r in iter_csv(z,'Observations.csv'):
    if not (r['Measure']=='A007233' and r['Opdrachtgever']=='T001209' and r['Eigendom']=='T001258'):continue
    regname=ALIASES.get(reg.get(r['RegioS'],{}).get('Title'), reg.get(r['RegioS'],{}).get('Title'));per=r['Perioden'];v=number(r['Value'])
    if regname not in SELECT or not re.fullmatch(r'\d{4}KW\d{2}',per) or v is None:continue
    yr=int(per[:4]);
    if yr<2015 or yr>2025:continue
    key=(yr,regname,r['RegioS']);permits[key]+=v;status[key].add(periods[per]['Status'])
rows=[]
for (yr,name,region),count in sorted(permits.items()):
    rows.append(dict(year=yr,municipality=name,region_code=region,
         permitted_dwellings=int(count),period_status='; '.join(sorted(status[(yr,name,region)])),source_id='83671NED'))
store('cbs_municipal_permits.csv',list(rows[0]),rows)
z.close()

print('COMPLETE: CBS bulk ZIP snapshots processed; check analysis limitations before interpretation.')
