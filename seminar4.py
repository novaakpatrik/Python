import json
from bokeh.plotting import ColumnDataSource, figure, show
from bokeh.models import LabelSet, ranges
from cmath import pi

file = open('election.json')
data = json.load(file)
    
names = []
shares = []
colors = []        
below_one_sum = 0

for party in data:
    if(party.get('share') < 1):
        below_one_sum += party.get('share')
        continue
    shares.append(party.get('share'))
    
    if 'short' in party:
        names.append(party.get('short'))
    else:
        names.append(party.get('name'))
        
    if 'color' in party:
        colors.append(party.get('color'))
    else:
        colors.append("#000000")

names.append("< 1%".format(below_one_sum))
shares.append("{:.2f}".format(below_one_sum))
colors.append("#696969")
x = range(0, len(shares))


def barplot():

    source = ColumnDataSource(dict(x = x,
                                   y = shares,
                                   names = names,
                                   color=colors))

    plot = figure(title = "Volby 2017",
                  x_axis_label = "Strany",
                  y_axis_label = "Hlasy v %")

    plot.vbar(source=source,
              x='x',
              top='y',
              bottom=0,
              width=0.7,
              color='color',
              legend='names')

    labels = LabelSet(x='x', y='y', text='y', level='glyph',
            x_offset=-13.5, y_offset=0, source=source, render_mode='canvas')
    plot.add_layout(labels)

    show(plot)
    
    
def piechart():

    shares2 = [0] + shares
    percents = []
    achieved = 0
    for share in shares2:
        achieved += (float(share) / 100)
        percents.append(achieved)

    source = ColumnDataSource(data={
        'start':[percent*2*pi for percent in percents[:-1]],
        'end':[percent*2*pi for percent in percents[1:]],
        'color':colors,
        'label': names,
        'value': percents[:-1]
    })

    plot = figure(x_range=(-1,1), y_range=(-1,1))
    plot.wedge(x=0, y=0, radius=1,
            start_angle='start',
            end_angle='end',
            color='color',
            legend='label',
            source=source)

    show(plot)

if __name__=='__main__':
    barplot()
