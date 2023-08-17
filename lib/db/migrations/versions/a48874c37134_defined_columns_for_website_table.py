"""defined columns for website table

Revision ID: a48874c37134
Revises: 9a9ab9bf9d0e
Create Date: 2023-08-17 16:46:34.249703

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a48874c37134'
down_revision: Union[str, None] = '9a9ab9bf9d0e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('websites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('websites')
    # ### end Alembic commands ###
