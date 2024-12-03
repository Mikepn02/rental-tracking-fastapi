"""Add tenants relationship to Property

Revision ID: 3387b3681a6c
Revises: 54dc2c1e96a1
Create Date: 2024-12-02 21:10:01.449899

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3387b3681a6c'
down_revision: Union[str, None] = '54dc2c1e96a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('properties', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'properties', 'users', ['owner_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'properties', type_='foreignkey')
    op.drop_column('properties', 'owner_id')
    # ### end Alembic commands ###