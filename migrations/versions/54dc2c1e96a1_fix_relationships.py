"""Fix relationships

Revision ID: 54dc2c1e96a1
Revises: 99cbad8a7522
Create Date: 2024-12-02 21:06:01.895740

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54dc2c1e96a1'
down_revision: Union[str, None] = '99cbad8a7522'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
