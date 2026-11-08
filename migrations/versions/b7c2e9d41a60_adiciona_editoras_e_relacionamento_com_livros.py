"""adiciona editoras e relacionamento com livros"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "b7c2e9d41a60"
down_revision: Union[str, Sequence[str], None] = "01ae3aa1664c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "editoras",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nome", sa.String(length=100), nullable=False),
        sa.Column("pais", sa.String(length=60), nullable=True),
        sa.Column("site", sa.String(length=200), nullable=True),
        sa.PrimaryKeyConstraint("id")
    )
    op.create_index(op.f("ix_editoras_id"), "editoras", ["id"], unique=False)
    op.add_column("livros", sa.Column("editora_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        "fk_livros_editoras", "livros", "editoras", ["editora_id"], ["id"],
        ondelete="SET NULL"
    )


def downgrade() -> None:
    op.drop_constraint("fk_livros_editoras", "livros", type_="foreignkey")
    op.drop_column("livros", "editora_id")
    op.drop_index(op.f("ix_editoras_id"), table_name="editoras")
    op.drop_table("editoras")
