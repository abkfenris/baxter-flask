"""initial changed srid

Revision ID: faceefe5e39
Revises: None
Create Date: 2015-01-13 22:26:39.349912

"""

# revision identifiers, used by Alembic.
revision = 'faceefe5e39'
down_revision = None

from alembic import op
import sqlalchemy as sa
import geoalchemy2


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('avalanche_paths',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('path', geoalchemy2.types.Geometry(geometry_type='POLYGON', srid=26919), nullable=True),
    sa.Column('aspect', sa.String(length=40), nullable=True),
    sa.Column('display', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('points_of_interests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('point', geoalchemy2.types.Geometry(geometry_type='POINT', srid=26919), nullable=True),
    sa.Column('bspaid', sa.String(length=40), nullable=True),
    sa.Column('poiid', sa.Integer(), nullable=True),
    sa.Column('poi_group', sa.String(length=40), nullable=True),
    sa.Column('poi_class', sa.String(length=40), nullable=True),
    sa.Column('poi_type', sa.String(length=40), nullable=True),
    sa.Column('remark', sa.Text(), nullable=True),
    sa.Column('elev_ft', sa.Float(), nullable=True),
    sa.Column('public_share', sa.Boolean(), nullable=True),
    sa.Column('site_capacity', sa.Integer(), nullable=True),
    sa.Column('facility_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='MULTILINESTRING', srid=26919), nullable=True),
    sa.Column('use_type', sa.String(length=40), nullable=True),
    sa.Column('tid', sa.Integer(), nullable=True),
    sa.Column('skitrail', sa.Boolean(), nullable=True),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('length_mi', sa.Float(), nullable=True),
    sa.Column('status', sa.String(length=40), nullable=True),
    sa.Column('display', sa.Boolean(), nullable=True),
    sa.Column('pubshare', sa.Boolean(), nullable=True),
    sa.Column('gpsupdate', sa.Date(), nullable=True),
    sa.Column('gpsunit', sa.String(length=40), nullable=True),
    sa.Column('gpsuser', sa.String(length=40), nullable=True),
    sa.Column('bspaid', sa.String(length=40), nullable=True),
    sa.Column('tsid', sa.String(length=40), nullable=True),
    sa.Column('display_wu', sa.Boolean(), nullable=True),
    sa.Column('display_wn', sa.Boolean(), nullable=True),
    sa.Column('ttype', sa.String(length=40), nullable=True),
    sa.Column('season', sa.String(length=40), nullable=True),
    sa.Column('shape_leng', sa.Float(), nullable=True),
    sa.Column('tclass', sa.String(length=40), nullable=True),
    sa.Column('maintclass', sa.String(length=40), nullable=True),
    sa.Column('slength', sa.Float(), nullable=True),
    sa.Column('min_slope', sa.Float(), nullable=True),
    sa.Column('max_slope', sa.Float(), nullable=True),
    sa.Column('avg_slope', sa.Float(), nullable=True),
    sa.Column('length_ft', sa.Float(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('confirmed_at', sa.DateTime(), nullable=True),
    sa.Column('observer', sa.Boolean(), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('first', sa.String(length=80), nullable=True),
    sa.Column('last', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('snowpits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=64), nullable=True),
    sa.Column('path', sa.Unicode(length=128), nullable=True),
    sa.Column('location', geoalchemy2.types.Geometry(geometry_type='POINT', srid=26919), nullable=True),
    sa.Column('elevation', sa.Integer(), nullable=True),
    sa.Column('aspect', sa.String(length=40), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('avalanche_problems',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('definition', sa.Text(), nullable=True),
    sa.Column('photo', sa.String(length=160), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('photoss',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=64), nullable=True),
    sa.Column('path', sa.Unicode(length=128), nullable=True),
    sa.Column('location', geoalchemy2.types.Geometry(geometry_type='POINT', srid=26919), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('weather_forecasts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('condition', sa.String(length=40), nullable=True),
    sa.Column('for_temp_high', sa.Integer(), nullable=True),
    sa.Column('for_temp_low', sa.Integer(), nullable=True),
    sa.Column('trail_comment', sa.Text(), nullable=True),
    sa.Column('for_today', sa.Text(), nullable=True),
    sa.Column('for_tomorrow', sa.Text(), nullable=True),
    sa.Column('for_long', sa.Text(), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('weather_observations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('sky', sa.String(length=40), nullable=True),
    sa.Column('precip_type', sa.String(length=40), nullable=True),
    sa.Column('precip_rate', sa.String(length=40), nullable=True),
    sa.Column('temp_max', sa.Float(), nullable=True),
    sa.Column('temp_min', sa.Float(), nullable=True),
    sa.Column('temp_present', sa.Float(), nullable=True),
    sa.Column('temp_trend', sa.String(length=40), nullable=True),
    sa.Column('pressure_present', sa.Float(), nullable=True),
    sa.Column('pressure_trend', sa.String(length=40), nullable=True),
    sa.Column('humidity', sa.Float(), nullable=True),
    sa.Column('wind_speed', sa.Float(), nullable=True),
    sa.Column('wind_direction', sa.String(length=40), nullable=True),
    sa.Column('wind_gust_max', sa.Float(), nullable=True),
    sa.Column('rain_24', sa.Float(), nullable=True),
    sa.Column('snow_depth', sa.Float(), nullable=True),
    sa.Column('snow_24', sa.Float(), nullable=True),
    sa.Column('snow_storm', sa.Float(), nullable=True),
    sa.Column('snow_8_temp', sa.Float(), nullable=True),
    sa.Column('snow_density', sa.Float(), nullable=True),
    sa.Column('snow_foot_pen', sa.Float(), nullable=True),
    sa.Column('snow_ram_pen', sa.Float(), nullable=True),
    sa.Column('snow_surface_form', sa.String(length=80), nullable=True),
    sa.Column('snow_surface_size', sa.Float(), nullable=True),
    sa.Column('snow_blowing_extent', sa.String(length=40), nullable=True),
    sa.Column('snow_water_equil', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('snowpits_photo',
    sa.Column('snowpit_id', sa.Integer(), nullable=True),
    sa.Column('photo_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['photo_id'], ['photoss.id'], ),
    sa.ForeignKeyConstraint(['snowpit_id'], ['snowpits.id'], )
    )
    op.create_table('avalanche_ins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('path_id', sa.Integer(), nullable=True),
    sa.Column('display', sa.Boolean(), nullable=True),
    sa.Column('observation_date', sa.DateTime(), nullable=True),
    sa.Column('occurence_date', sa.DateTime(), nullable=True),
    sa.Column('location', sa.Text(), nullable=True),
    sa.Column('elevation', sa.Integer(), nullable=True),
    sa.Column('aspect', sa.String(length=40), nullable=True),
    sa.Column('trigger', sa.String(length=40), nullable=True),
    sa.Column('trigger_add', sa.String(length=40), nullable=True),
    sa.Column('av_problem', sa.String(length=40), nullable=True),
    sa.Column('av_type', sa.String(length=40), nullable=True),
    sa.Column('weak_layer', sa.String(length=40), nullable=True),
    sa.Column('size_relative', sa.Float(), nullable=True),
    sa.Column('size_desctructive', sa.Float(), nullable=True),
    sa.Column('depth', sa.Float(), nullable=True),
    sa.Column('width', sa.Float(), nullable=True),
    sa.Column('vertical', sa.Float(), nullable=True),
    sa.Column('slope_angle', sa.Float(), nullable=True),
    sa.Column('people_caught', sa.Integer(), nullable=True),
    sa.Column('people_carried', sa.Integer(), nullable=True),
    sa.Column('people_injured', sa.Integer(), nullable=True),
    sa.Column('people_buried_part', sa.Integer(), nullable=True),
    sa.Column('people_buried_full', sa.Integer(), nullable=True),
    sa.Column('people_killed', sa.Integer(), nullable=True),
    sa.Column('people_rescuer', sa.Integer(), nullable=True),
    sa.Column('group_activity', sa.String(length=40), nullable=True),
    sa.Column('group_travel', sa.String(length=40), nullable=True),
    sa.Column('snow_profile', sa.Text(), nullable=True),
    sa.Column('image', sa.String(length=160), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('summary', sa.Text(), nullable=True),
    sa.Column('crown', geoalchemy2.types.Geometry(geometry_type='MULTILINESTRING', srid=26919), nullable=True),
    sa.Column('bed_surface', geoalchemy2.types.Geometry(geometry_type='MULTIPOLYGON', srid=26919), nullable=True),
    sa.Column('debris_field', geoalchemy2.types.Geometry(geometry_type='MULTIPOLYGON', srid=26919), nullable=True),
    sa.ForeignKeyConstraint(['path_id'], ['avalanche_paths.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trails_photo',
    sa.Column('trail_id', sa.Integer(), nullable=True),
    sa.Column('photo_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['photo_id'], ['photoss.id'], ),
    sa.ForeignKeyConstraint(['trail_id'], ['trails.id'], )
    )
    op.create_table('avalanche_involved',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('incident_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('first', sa.String(length=40), nullable=True),
    sa.Column('last', sa.String(length=40), nullable=True),
    sa.Column('phone', sa.String(length=40), nullable=True),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.Column('info', sa.Text(), nullable=True),
    sa.Column('observed', sa.Boolean(), nullable=True),
    sa.Column('group', sa.Boolean(), nullable=True),
    sa.Column('caught', sa.Boolean(), nullable=True),
    sa.Column('carried', sa.Boolean(), nullable=True),
    sa.Column('burried', sa.Boolean(), nullable=True),
    sa.Column('rescuer', sa.Boolean(), nullable=True),
    sa.Column('locations', geoalchemy2.types.Geometry(geometry_type='MULTIPOINT', srid=26919), nullable=True),
    sa.ForeignKeyConstraint(['incident_id'], ['avalanche_ins.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('avalanche_ins_snowpit',
    sa.Column('avalanche_ins_id', sa.Integer(), nullable=True),
    sa.Column('snowpit_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['avalanche_ins_id'], ['avalanche_ins.id'], ),
    sa.ForeignKeyConstraint(['snowpit_id'], ['snowpits.id'], )
    )
    op.create_table('avalanche_ob_problem',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('incident_id', sa.Integer(), nullable=True),
    sa.Column('problem_id', sa.Integer(), nullable=True),
    sa.Column('importance', sa.Integer(), nullable=True),
    sa.Column('aspects', sa.String(length=80), nullable=True),
    sa.Column('likelyhood', sa.String(length=40), nullable=True),
    sa.Column('size', sa.String(length=40), nullable=True),
    sa.Column('trend', sa.String(length=40), nullable=True),
    sa.Column('discussion', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['incident_id'], ['avalanche_ins.id'], ),
    sa.ForeignKeyConstraint(['problem_id'], ['avalanche_problems.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('avalanche_ins_photo',
    sa.Column('avalanche_ins_id', sa.Integer(), nullable=True),
    sa.Column('photo_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['avalanche_ins_id'], ['avalanche_ins.id'], ),
    sa.ForeignKeyConstraint(['photo_id'], ['photoss.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('avalanche_ins_photo')
    op.drop_table('avalanche_ob_problem')
    op.drop_table('avalanche_ins_snowpit')
    op.drop_table('avalanche_involved')
    op.drop_table('trails_photo')
    op.drop_table('avalanche_ins')
    op.drop_table('snowpits_photo')
    op.drop_table('weather_observations')
    op.drop_table('roles_users')
    op.drop_table('weather_forecasts')
    op.drop_table('photoss')
    op.drop_table('avalanche_problems')
    op.drop_table('snowpits')
    op.drop_table('users')
    op.drop_table('trails')
    op.drop_table('points_of_interests')
    op.drop_table('roles')
    op.drop_table('avalanche_paths')
    ### end Alembic commands ###
