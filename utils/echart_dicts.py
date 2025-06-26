import numpy as np

class Bar:
    # Class attributes
    bm_plotrange = np.arange(0, 3000, 50)
    bm_hist = {
        'title': {
            'text': 'Biomass variability',
            'left': "left"},
        'tooltip': {},
        'legend': {},
        'grid': {'show': False,
                 'left': '20%', 'bottom': 60},
        'xAxis': {
            'type': 'value',
            'name': 'Biomass (lbs/ac)',
            'nameLocation': 'middle',
            'nameGap': 30,
            'splitLine': {
                'show': False}},
        'yAxis': {'max': 100,
                  'axisLabel': {'formatter': '{value} %'},
                  'splitLine': {
                      'show': False}},
        'series': [{
            'name': "",
            'type': "bar",
            'data': [{'value': [x, 0]} for idx, x in enumerate(bm_plotrange)],
            'colorBy': "data"}]}

    thresh_labels = ['Unlikely', 'Less likely', 'Possible', 'More likely', 'Likely']
    thresh_bar = {
        'title': {
            'text': "Biomass threshold",
            'left': "left"},
        'tooltip': {},
        'legend': {},
        'grid': {'left': '20%', 'bottom': 60},
        'xAxis': {
            'type': 'category',
            'name': 'Probability of biomass less than threshold',
            'nameLocation': 'middle',
            'nameGap': 30,
            'data': thresh_labels},
        'yAxis': {'max': 1000,
                  'axisLabel': {'formatter': '{value} ac.'}},
        'series': [{
            'name': "",
            'type': "bar",
            'data': [0 for x in thresh_labels],
            'colorBy': "data"
        }],
    }

class Pie:
    # Class attributes
    cov_pie = {
        'title': {
            'text': "Cover",
            'subtext': "Fractional vegetation cover (%)",
            'left': "left"},
        'grid': [{'bottom': 10}],
        'tooltip': {'show': True,
                    'formatter': '{b}: {d} %'}, 
        'series': [{
            'type': 'pie',
            'data': [{'value': 0, 'name': 'Litter'},
                     {'value': 0, 'name': 'Bare ground'},
                     {'value': 0, 'name': 'Green veg'},
                     {'value': 0, 'name': 'Dry veg'}],
            'color': ['#ee6666', '#91cc75', '#5470c6', '#fac858'],
            'roseType': 'radius',
            'radius': ["0%", "45%"],
            'label': {
                'edgeDistance': "1%",
                'bleedMargin': 10,
                'alignTo': "edge"},
            'labelLine': {'length': 5}}]}

class Line:
    def __init__(self, aoi_means=None, map_yr=None, comp_yr=None):
        self.past_col = '#d95f02'
        self.poly_col = '#1b9e77'
        self.aoi_means = aoi_means
        self.map_yr = map_yr
        self.comp_yr = comp_yr

        self.ts_cov = {
            'title': [{'left': 'left', 'text': 'Cover (Pasture)'}],
            'grid': [{'bottom': 40}],
            'tooltip': {'trigger': 'axis'},
            'xAxis': [{'type': 'time'}],
            'yAxis': [{'max': 100}],
            'series': [{'name': 'Bare',
                        'type': 'line',
                        'detail': '{value} %',
                       'stack': 'x',
                       'areaStyle': {},
                        'showSymbol': False,
                        'data': [],
                        'itemStyle': {'color': 'rgb(0, 0, 200)'},
                        'lineStyle': {'type': 'solid'}},
                      {'name': 'Litter',
                       'type': 'line',
                        'detail': '{value} %',
                       'stack': 'x',
                       'areaStyle': {},
                       'showSymbol': False,
                       'data': [],
                       'itemStyle': {'color': 'rgb(200, 200, 10)'},
                       'lineStyle': {'type': 'solid'}},
                      {'name': 'Dry',
                        'type': 'line',
                        'detail': '{value} %',
                       'stack': 'x',
                       'areaStyle': {},
                        'showSymbol': False,
                        'data': [],
                        'itemStyle': {'color': 'rgb(200, 0, 0)'},
                        'lineStyle': {'type': 'solid'}},
                      {'name': 'Green',
                        'type': 'line',
                        'detail': '{value} %',
                       'stack': 'x',
                       'areaStyle': {},
                        'showSymbol': False,
                        'data': [],
                        'itemStyle': {'color': 'rgb(0, 175, 0)'}, 
                        'lineStyle': {'type': 'solid'}}]}
        
        if self.aoi_means is not None:
            self.ts_bm = {
                'title': [{'left': 'left', 'top': 20, 'text': 'Biomass'}],
                'grid': [{'bottom': 40}],
                'legend': {'orient': 'vertical',
                           'right': 10,
                           'top': 20,
                           'data': [{'name': 'long-term avg.',
                                     'icon': 'path://M180 1000 l0 -30 200 0 200 0 0 30 0 30 -200 0 -200 0 0 -30z'},
                                    {'name': 'TRM',
                                     'icon': 'path://M180 1000 l0 -30 200 0 200 0 0 30 0 30 -200 0 -200 0 0 -30z'},
                                    {'name': 'Heavy',
                                     'icon': 'path://M180 1000 l0 -30 200 0 200 0 0 30 0 30 -200 0 -200 0 0 -30z'}]},
                'tooltip': {'trigger': 'axis'},
                'xAxis': [{'type': 'time'}],
                'yAxis': [{'min': 0,
                           'max': 3000}],
                'series': [{'name': 'long-term avg.',
                            'type': 'line',
                            'showSymbol': False,
                            'data': list(map(list, zip(self.aoi_means[(self.aoi_means['Pasture'] == 'cper') & 
                                                       (self.aoi_means['Year'] == 'long-term avg.')]['date'],
                                                       self.aoi_means[(self.aoi_means['Pasture'] == 'cper') & 
                                                       (self.aoi_means['Year'] == 'long-term avg.')]['Biomass']))),
                            'itemStyle': {'color': 'black'}
                           },
                           {'name': str(comp_yr),
                            'type': 'line',
                            'showSymbol': False,
                            'data': list(map(list, zip(self.aoi_means[(self.aoi_means['Pasture'] == 'cper') & 
                                                       (self.aoi_means['Year'] == str(self.comp_yr))]['date'],
                                                       self.aoi_means[(self.aoi_means['Pasture'] == 'cper') & 
                                                       (self.aoi_means['Year'] == str(self.comp_yr))]['Biomass']))),
                            'itemStyle': {'color': 'black'},
                            'lineStyle': {'width': 1,
                                          'type': 'dotted'}
                           },
                           {'name': 'Pasture',
                            'type': 'line',
                            'showSymbol': False,
                            'data': [],
                            'itemStyle': {'color': self.past_col}
                           },
                           {'name': 'Drawing',
                            'type': 'line',
                            'showSymbol': False,
                            'data': [],
                            'itemStyle': {'color': self.poly_col}
                           },
                           {'name': 'Raw observation',
                            'type': 'scatter',
                            'data': [],
                            'symbolSize': 4,
                            'itemStyle': {'color': self.past_col}
                           },
                           {'name': 'TRM',
                            'type': 'line',
                            'showSymbol': False,
                            'data': list(map(list, zip(self.aoi_means[(self.aoi_means['Pasture'] == 'TRM') & 
                                                       (self.aoi_means['Year'] == str(self.map_yr))]['date'],
                                                       self.aoi_means[(self.aoi_means['Pasture'] == 'TRM') & 
                                                       (self.aoi_means['Year'] == str(self.map_yr))]['Biomass']))),
                            'itemStyle': {'color': '#33ceff'}
                           },
                           {'name': 'Heavy',
                            'type': 'line',
                            'showSymbol': False,
                            'data': list(map(list, zip(self.aoi_means[(self.aoi_means['Pasture'] == 'Heavy') & 
                                                       (self.aoi_means['Year'] == str(self.map_yr))]['date'],
                                                       self.aoi_means[(self.aoi_means['Pasture'] == 'Heavy') & 
                                                       (self.aoi_means['Year'] == str(self.map_yr))]['Biomass']))),
                            'itemStyle': {'color': '#ff333c'}
                           }
                          ]
            }    

            self.ts_ndvi = {
                'title': [{'left': 'left', 'text': 'Greenness (NDVI)'}],
                'grid': [{'bottom': 40}],
                'legend': {'orient': 'vertical',
                           'right': 10,
                           'top': 'top',
                           'data': [{'name': 'long-term avg.',
                                     'icon': 'path://M180 1000 l0 -30 200 0 200 0 0 30 0 30 -200 0 -200 0 0 -30z'},
                                    {'name': 'TRM',
                                     'icon': 'path://M180 1000 l0 -30 200 0 200 0 0 30 0 30 -200 0 -200 0 0 -30z'},
                                    {'name': 'Heavy',
                                     'icon': 'path://M180 1000 l0 -30 200 0 200 0 0 30 0 30 -200 0 -200 0 0 -30z'}]},
                'tooltip': {'trigger': 'axis'},
                'xAxis': [{'type': 'time'}],
                'yAxis': [{'max': 0.8}],
                'series': [{'name': 'long-term avg.',
                            'type': 'line',
                            'showSymbol': False,
                            'data': list(map(list, zip(self.aoi_means[(self.aoi_means['Pasture'] == 'cper') & 
                                                       (self.aoi_means['Year'] == 'long-term avg.')]['date'],
                                                       self.aoi_means[(self.aoi_means['Pasture'] == 'cper') & 
                                                       (self.aoi_means['Year'] == 'long-term avg.')]['NDVI']))),
                            'itemStyle': {'color': 'black'}
                           },
                           {'name': str(self.comp_yr),
                            'type': 'line',
                            'showSymbol': False,
                            'data': list(map(list, zip(self.aoi_means[(self.aoi_means['Pasture'] == 'cper') & 
                                                       (self.aoi_means['Year'] == str(self.comp_yr))]['date'],
                                                       self.aoi_means[(self.aoi_means['Pasture'] == 'cper') & 
                                                       (self.aoi_means['Year'] == str(self.comp_yr))]['NDVI']))),
                            'itemStyle': {'color': 'black'},
                            'lineStyle': {'width': 1,
                                          'type': 'dotted'}
                           },
                           {'name': 'Pasture (' + str(self.map_yr) + ')',
                            'type': 'line',
                            'showSymbol': False,
                            'data': [],
                            'itemStyle': {'color': self.past_col}
                           },
                           {'name': 'Drawing',
                            'type': 'line',
                            'showSymbol': False,
                            'data': [],
                            'itemStyle': {'color': self.poly_col}
                           },
                           {'name': 'Raw observation',
                            'type': 'scatter',
                            'data': [],
                            'symbolSize': 4,
                            'itemStyle': {'color': self.past_col}
                           },
                           {'name': 'TRM',
                            'type': 'line',
                            'showSymbol': False,
                            'data': list(map(list, zip(self.aoi_means[(self.aoi_means['Pasture'] == 'TRM') & 
                                                       (self.aoi_means['Year'] == str(self.map_yr))]['date'],
                                                       self.aoi_means[(self.aoi_means['Pasture'] == 'TRM') & 
                                                       (self.aoi_means['Year'] == str(self.map_yr))]['NDVI']))),
                            'itemStyle': {'color': '#33ceff'}
                           },
                           {'name': 'Heavy',
                            'type': 'line',
                            'showSymbol': False,
                            'data': list(map(list, zip(self.aoi_means[(self.aoi_means['Pasture'] == 'Heavy') & 
                                                       (self.aoi_means['Year'] == str(self.map_yr))]['date'],
                                                       self.aoi_means[(self.aoi_means['Pasture'] == 'Heavy') & 
                                                       (self.aoi_means['Year'] == str(self.map_yr))]['NDVI']))),
                            'itemStyle': {'color': '#ff333c'}
                           }
                          ]
            }   

            self.ts_cp = {
                'title': [{'left': 'left', 'text': 'Crude protein'}],
                'grid': [{'bottom': 40}],
                'legend': {'orient': 'vertical',
                           'right': 10,
                           'top': 'top',
                           'data': [{'name': 'long-term avg.',
                                     'icon': 'path://M180 1000 l0 -30 200 0 200 0 0 30 0 30 -200 0 -200 0 0 -30z'},
                                    {'name': 'TRM',
                                     'icon': 'path://M180 1000 l0 -30 200 0 200 0 0 30 0 30 -200 0 -200 0 0 -30z'},
                                    {'name': 'Heavy',
                                     'icon': 'path://M180 1000 l0 -30 200 0 200 0 0 30 0 30 -200 0 -200 0 0 -30z'}]},
                'tooltip': {'trigger': 'axis'},
                'xAxis': [{'type': 'time'}],
                'yAxis': [{'max': 14,
                           'min': 4}],
                'series': [{'name': 'long-term avg.',
                            'type': 'line',
                            'showSymbol': False,
                            'data': list(map(list, zip(self.aoi_means[(self.aoi_means['Pasture'] == 'cper') & 
                                                       (self.aoi_means['Year'] == 'long-term avg.')]['date'],
                                                       self.aoi_means[(self.aoi_means['Pasture'] == 'cper') & 
                                                       (self.aoi_means['Year'] == 'long-term avg.')]['CP']))),
                            'itemStyle': {'color': 'black'}
                           },
                           {'name': str(self.comp_yr),
                            'type': 'line',
                            'showSymbol': False,
                            'data': list(map(list, zip(self.aoi_means[(self.aoi_means['Pasture'] == 'cper') & 
                                                       (self.aoi_means['Year'] == str(self.comp_yr))]['date'],
                                                       self.aoi_means[(self.aoi_means['Pasture'] == 'cper') & 
                                                       (self.aoi_means['Year'] == str(self.comp_yr))]['CP']))),
                            'itemStyle': {'color': 'black'},
                            'lineStyle': {'width': 1,
                                          'type': 'dotted'}
                           },
                           {'name': 'Pasture (' + str(self.map_yr) + ')',
                            'type': 'line',
                            'showSymbol': False,
                            'data': [],
                            'itemStyle': {'color': self.past_col}
                           },
                           {'name': 'Drawing',
                            'type': 'line',
                            'showSymbol': False,
                            'data': [],
                            'itemStyle': {'color': self.poly_col}
                           },
                           {'name': 'TRM',
                            'type': 'line',
                            'showSymbol': False,
                            'data': list(map(list, zip(self.aoi_means[(self.aoi_means['Pasture'] == 'TRM') & 
                                                       (self.aoi_means['Year'] == str(self.map_yr))]['date'],
                                                       self.aoi_means[(self.aoi_means['Pasture'] == 'TRM') & 
                                                       (self.aoi_means['Year'] == str(self.map_yr))]['CP']))),
                            'itemStyle': {'color': '#33ceff'}
                           },
                           {'name': 'Heavy',
                            'type': 'line',
                            'showSymbol': False,
                            'data': list(map(list, zip(self.aoi_means[(self.aoi_means['Pasture'] == 'Heavy') & 
                                                       (self.aoi_means['Year'] == str(self.map_yr))]['date'],
                                                       self.aoi_means[(self.aoi_means['Pasture'] == 'Heavy') & 
                                                       (self.aoi_means['Year'] == str(self.map_yr))]['CP']))),
                            'itemStyle': {'color': '#ff333c'}
                           }
                          ]
            }   

        