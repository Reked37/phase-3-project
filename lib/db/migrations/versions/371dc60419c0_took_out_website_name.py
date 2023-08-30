"""took out website_name

Revision ID: 371dc60419c0
Revises: d36ea5069018
Create Date: 2023-08-29 18:21:40.069981

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '371dc60419c0'
down_revision: Union[str, None] = 'd36ea5069018'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'website_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('website_name', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###