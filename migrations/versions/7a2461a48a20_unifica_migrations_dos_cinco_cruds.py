"""unifica migrations dos cinco CRUDs

Revision ID: 7a2461a48a20
Revises: 937c2fa67ee6, b7c2e9d41a60
Create Date: 2026-11-08 13:20:28.223941

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a2461a48a20'
down_revision: Union[str, Sequence[str], None] = ('937c2fa67ee6', 'b7c2e9d41a60')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
