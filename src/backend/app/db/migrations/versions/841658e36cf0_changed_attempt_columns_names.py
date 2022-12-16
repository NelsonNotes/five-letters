"""changed attempt columns names

Revision ID: 841658e36cf0
Revises: af134fc51ebb
Create Date: 2022-12-15 18:19:29.985317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '841658e36cf0'
down_revision = 'af134fc51ebb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attempt', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('attempt', sa.Column('word_id', sa.Integer(), nullable=True))
    op.drop_constraint('attempt_userId_fkey', 'attempt', type_='foreignkey')
    op.drop_constraint('attempt_wordId_fkey', 'attempt', type_='foreignkey')
    op.create_foreign_key(None, 'attempt', 'word', ['word_id'], ['id'])
    op.create_foreign_key(None, 'attempt', 'user', ['user_id'], ['id'])
    op.drop_column('attempt', 'wordId')
    op.drop_column('attempt', 'userId')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attempt', sa.Column('userId', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('attempt', sa.Column('wordId', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'attempt', type_='foreignkey')
    op.drop_constraint(None, 'attempt', type_='foreignkey')
    op.create_foreign_key('attempt_wordId_fkey', 'attempt', 'word', ['wordId'], ['id'])
    op.create_foreign_key('attempt_userId_fkey', 'attempt', 'user', ['userId'], ['id'])
    op.drop_column('attempt', 'word_id')
    op.drop_column('attempt', 'user_id')
    # ### end Alembic commands ###
