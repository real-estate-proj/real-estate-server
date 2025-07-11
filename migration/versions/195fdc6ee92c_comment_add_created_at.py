"""comment: add - created_at

Revision ID: 195fdc6ee92c
Revises: ffcd5fb5c225
Create Date: 2025-06-16 11:41:41.099173

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '195fdc6ee92c'
down_revision: Union[str, None] = 'ffcd5fb5c225'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('created_at', sa.TIMESTAMP(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'created_at')
    # ### end Alembic commands ###
