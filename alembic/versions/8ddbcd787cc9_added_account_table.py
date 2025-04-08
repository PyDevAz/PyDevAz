"""added account table

Revision ID: 8ddbcd787cc9
Revises: 6a698ef06780
Create Date: 2025-03-24 12:01:40.803953

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ddbcd787cc9'
down_revision: Union[str, None] = '6a698ef06780'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('type', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('categories', 'type')
    # ### end Alembic commands ###
