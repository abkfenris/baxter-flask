"""remove incident_id from snowpit

Revision ID: 16795fbb1c06
Revises: 129da6a086ef
Create Date: 2015-01-04 21:14:49.489325

"""

# revision identifiers, used by Alembic.
revision = '16795fbb1c06'
down_revision = '129da6a086ef'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    #op.drop_index('idx_avalanche_ins_bed_surface', table_name='avalanche_ins')
    #op.drop_index('idx_avalanche_ins_crown', table_name='avalanche_ins')
    #op.drop_index('idx_avalanche_ins_debris_field', table_name='avalanche_ins')
    #op.drop_index('idx_avalanche_paths_path', table_name='avalanche_paths')
    #op.drop_index('idx_photoss_location', table_name='photoss')
    #op.drop_index('idx_points_of_interests_point', table_name='points_of_interests')
    #op.drop_index('idx_snowpits_location', table_name='snowpits')
    op.drop_constraint(u'snowpits_incident_id_fkey', 'snowpits', type_='foreignkey')
    op.drop_column('snowpits', 'incident_id')
    #op.drop_index('idx_trails_geom', table_name='trails')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    #op.create_index('idx_trails_geom', 'trails', ['geom'], unique=False)
    op.add_column('snowpits', sa.Column('incident_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key(u'snowpits_incident_id_fkey', 'snowpits', 'avalanche_ins', ['incident_id'], ['id'])
    #op.create_index('idx_snowpits_location', 'snowpits', ['location'], unique=False)
    #op.create_index('idx_points_of_interests_point', 'points_of_interests', ['point'], unique=False)
    #op.create_index('idx_photoss_location', 'photoss', ['location'], unique=False)
    #op.create_index('idx_avalanche_paths_path', 'avalanche_paths', ['path'], unique=False)
    #op.create_index('idx_avalanche_ins_debris_field', 'avalanche_ins', ['debris_field'], unique=False)
    #op.create_index('idx_avalanche_ins_crown', 'avalanche_ins', ['crown'], unique=False)
    #op.create_index('idx_avalanche_ins_bed_surface', 'avalanche_ins', ['bed_surface'], unique=False)
    ### end Alembic commands ###