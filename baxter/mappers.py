"""
Mapping dicts from database/observation shorthand
"""

from collections import OrderedDict

aspects = OrderedDict([('unknown', 'Unknown'),
                       ('N', 'North'),
                       ('NE', 'North East'),
                       ('E', 'East'),
                       ('SE', 'South East'),
                       ('S', 'South'),
                       ('SW', 'South West'),
                       ('W', 'West'),
                       ('NW', 'North West')
                       ])

directions = OrderedDict([('N', 'North'),
                          ('NE', 'North East'),
                          ('E', 'East'),
                          ('SE', 'South East'),
                          ('S', 'South'),
                          ('SW', 'South West'),
                          ('W', 'West'),
                          ('NW', 'North West')
                          ])

triggers = OrderedDict([('unknown', 'Unknown'),
                        ('natural', 'Natural'),
                        ('skier', 'Skier'),
                        ('snowboarder', 'Snowboarder'),
                        ('snowmobiler', 'Snowmobiler'),
                        ('snowbike', 'Snow Bike'),
                        ('snowshoer', 'Snowshoer'),
                        ('explosive', 'Explosive'),
                        ('hiker', 'Hiker'),
                        ('other', 'Other')
                        ])

triggers_add = OrderedDict([('unknown', 'Unknown'),
                            ('intentional', 'Intentionally Triggered'),
                            ('unintentional', 'Unintentionally Triggered'),
                            ('remote', 'Remotely Triggered'),
                            ('cornice', 'Cornice Triggered'),
                            ('sympathetic', 'Sympathetic Release'),
                            ('repeater', 'Repeater')
                            ])

av_problems = OrderedDict([('unknown', 'Unknown'),
                           ('storm', 'Storm Slab'),
                           ('persistent', 'Persistant Slab'),
                           ('deep', 'Deep Slab'),
                           ('wet', 'Wet Slab'),
                           ('loosedry', 'Loose Dry Snow'),
                           ('loosewet', 'Loose Wet Snow'),
                           ('wind', 'Wind Slab'),
                           ('cornice', 'Cornice'),
                           ('glide', 'Glide')
                           ])

av_types = OrderedDict([('U', 'Unknown'),
                        ('L', 'Dry Loose'),
                        ('SS', 'Soft Slab'),
                        ('HS', 'Hard Slab'),
                        ('WL', 'Wet Loose'),
                        ('WS', 'Wet Slab'),
                        ('C', 'Cornice Fall'),
                        ('I', 'Ice fall'),
                        ('SF', 'Slush flow'),
                        ('R', 'Roof Avalanche'),
                        ])

weak_layers = OrderedDict([('unknown', 'Unknown'),
                           ('new', 'New Snow'),
                           ('density', 'Density Change'),
                           ('interface', 'New Snow/Old Snow Interface'),
                           ('facets', 'Facets'),
                           ('depth', 'Depth Hoar'),
                           ('surface', 'Surface Hoar'),
                           ('graupel', 'Graupel'),
                           ('wetgrains', 'Wet Grains'),
                           ('ground', 'Ground Interface')
                           ])

conditions = OrderedDict([('GREEN', 'Green - Favorable Conditions'),
                          ('YELLOW', 'Yellow - Favorable but Deteriorating Conditions'),
                          ('RED', 'Red - Above Treeline and Technical Activities Not Recomended')
                          ])

sky_covers = OrderedDict([('CLR', 'Clear'),
                          ('FEW', 'Few Clouds'),
                          ('SCT', 'Scattered Clouds'),
                          ('BKN', 'Broken Clouds'),
                          ('OVC', 'Overcast'),
                          ('X', 'Obscured')
                          ])

precip_types = OrderedDict([('NO', 'No Percipitation'),
                            ('RA', 'Rain'),
                            ('SN', 'Snow'),
                            ('RS', 'Mixed Rain and Snow'),
                            ('GR', 'Gaupel and Hail'),
                            ('ZR', 'Freezing Rain')
                            ])

precip_rates = OrderedDict([('NO', 'No Precipitation'),
                            ('S-1', 'S-1 - Very Light Snowfall (trace to .25in)'),
                            ('S1', 'S1 - Light Snowfall (.5 in)'),
                            ('S2', 'S2 - Moderate Snowfall (1 in)'),
                            ('S5', 'S5 - Heavy Snowfall (2 in)'),
                            ('S10', 'S10 - Very Heavy Snowfall (4 in)'),
                            ('RV', 'RV - Very Light Rain (no accumulation)'),
                            ('RL', 'RL - Light Rain'),
                            ('RM', 'RM - Moderate Rain'),
                            ('RH', 'RH - Heavy Rain')
                            ])

temp_trends = OrderedDict([('RR', 'RR - Rising Rapidly (more than 10F)'),
                           ('R', 'R - Rising (2-10F)'),
                           ('S', 'S - Steady'),
                           ('F', 'F - Falling (2-10F)'),
                           ('FR', 'FR - Falling Rapidly (more than 10F)')
                           ])

pressure_trends = OrderedDict([('RR', 'RR - Rising Rapidly (greater than 2 mb)'),
                               ('R', 'R - Rising (less than 2 mb)'),
                               ('S', 'S - Steady (less than 1 mb in 3 hours'),
                               ('F', 'F - Falling (less than 2 mb)'),
                               ('FR', 'FR - Falling Rapidly (more than 2 mb)')
                               ])
