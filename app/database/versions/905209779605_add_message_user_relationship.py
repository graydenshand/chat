"""add message <> user relationship

Revision ID: 905209779605
Revises: 
Create Date: 2020-05-16 21:38:48.679460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '905209779605'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('messages',
    	sa.Column('user_id', sa.Integer, sa.ForeignKey("users.id"))
    )


def downgrade():
    op.drop_column('messages', 'user_id')
