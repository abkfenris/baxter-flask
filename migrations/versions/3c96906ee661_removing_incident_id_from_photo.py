"""removing incident_id from photo

Revision ID: 3c96906ee661
Revises: 76489d1e0d5
Create Date: 2015-01-04 20:53:08.009678

"""

# revision identifiers, used by Alembic.
revision = '3c96906ee661'
down_revision = '76489d1e0d5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    print 'Drop Constraint'
    op.drop_constraint(None, 'photoss', type_='foreignkey')
    print 'Drop column'
    op.drop_column('photoss', 'incident_id')


def downgrade():
    op.add_column('photoss', sa.Column('incident_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'photoss', 'avalanche_ins', ['incident_id'], ['id'])
