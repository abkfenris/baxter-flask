"""Flask-security User and Roles

Revision ID: 1f9881c44228
Revises: 33f86343dd78
Create Date: 2014-12-18 07:26:53.482849

"""

# revision identifiers, used by Alembic.
revision = '1f9881c44228'
down_revision = '33f86343dd78'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    #op.drop_index('idx_avalanche_ins_bed_surface', table_name='avalanche_ins')
    #op.drop_index('idx_avalanche_ins_crown', table_name='avalanche_ins')
    #op.drop_index('idx_avalanche_ins_debris_field', table_name='avalanche_ins')
    #op.drop_index('idx_avalanche_paths_path', table_name='avalanche_paths')
    #op.drop_index('idx_photoss_location', table_name='photoss')
    #op.drop_index('idx_points_of_interests_point', table_name='points_of_interests')
    #op.drop_index('idx_snowpits_location', table_name='snowpits')
    #op.drop_index('idx_trails_geom', table_name='trails')
    op.add_column(u'users', sa.Column('active', sa.Boolean(), nullable=True))
    op.add_column(u'users', sa.Column('confirmed_at', sa.DateTime(), nullable=True))
    op.add_column(u'users', sa.Column('password', sa.String(length=255), nullable=True))
    op.drop_column(u'users', 'password_hash')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'users', sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    op.drop_column(u'users', 'password')
    op.drop_column(u'users', 'confirmed_at')
    op.drop_column(u'users', 'active')
    #op.create_index('idx_trails_geom', 'trails', ['geom'], unique=False)
    #op.create_index('idx_snowpits_location', 'snowpits', ['location'], unique=False)
    #op.create_index('idx_points_of_interests_point', 'points_of_interests', ['point'], unique=False)
    #op.create_index('idx_photoss_location', 'photoss', ['location'], unique=False)
    #op.create_index('idx_avalanche_paths_path', 'avalanche_paths', ['path'], unique=False)
    #op.create_index('idx_avalanche_ins_debris_field', 'avalanche_ins', ['debris_field'], unique=False)
    #op.create_index('idx_avalanche_ins_crown', 'avalanche_ins', ['crown'], unique=False)
    #op.create_index('idx_avalanche_ins_bed_surface', 'avalanche_ins', ['bed_surface'], unique=False)
    op.drop_table('roles_users')
    op.drop_table('roles')
    ### end Alembic commands ###
