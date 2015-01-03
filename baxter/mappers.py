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
