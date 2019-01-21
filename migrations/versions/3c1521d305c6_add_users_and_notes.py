"""add users and notes

Revision ID: 3c1521d305c6
Revises: 
Create Date: 2019-01-19 13:30:14.801163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c1521d305c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('username', sa.Unicode(length=64), nullable=False),
    sa.Column('password', sa.Unicode(length=80), nullable=False),
    sa.PrimaryKeyConstraint('username')
    )
    op.create_table('notes',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.UnicodeText(), nullable=False),
    sa.Column('public', sa.Boolean(), nullable=False),
    sa.Column('username', sa.Unicode(length=64), nullable=False),
    sa.ForeignKeyConstraint(['username'], ['users.username'], name='notes_author_fkey'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notes')
    op.drop_table('users')
    # ### end Alembic commands ###