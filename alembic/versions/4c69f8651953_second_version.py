"""second_version

Revision ID: 4c69f8651953
Revises: 98ebe3f9b68e
Create Date: 2024-10-14 17:30:19.061723

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c69f8651953'
down_revision: Union[str, None] = '98ebe3f9b68e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User_data', sa.Column('mobile', sa.String(length=10), nullable=True))
    op.create_unique_constraint(None, 'User_data', ['mobile'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'User_data', type_='unique')
    op.drop_column('User_data', 'mobile')
    # ### end Alembic commands ###
