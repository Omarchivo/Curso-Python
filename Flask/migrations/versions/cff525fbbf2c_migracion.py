"""Migracion

Revision ID: cff525fbbf2c
Revises: 
Create Date: 2024-01-06 19:04:12.153210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cff525fbbf2c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('nombre', sa.String(length=120), nullable=True),
    sa.Column('password_encriptada', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_usuarios_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_usuarios_nombre'), ['nombre'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_usuarios_nombre'))
        batch_op.drop_index(batch_op.f('ix_usuarios_email'))

    op.drop_table('usuarios')
    # ### end Alembic commands ###
