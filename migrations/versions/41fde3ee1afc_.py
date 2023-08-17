"""empty message

Revision ID: 41fde3ee1afc
Revises: 44071ece32e8
Create Date: 2023-08-16 22:57:55.892353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41fde3ee1afc'
down_revision = '44071ece32e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite_characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('related_user', sa.Integer(), nullable=False),
    sa.Column('favorite_characters', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['favorite_characters'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['related_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite_planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('related_user', sa.Integer(), nullable=False),
    sa.Column('favorite_planets', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['favorite_planets'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['related_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('favorites')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorites',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('related_user', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('favorite_characters', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('favorite_planets', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['favorite_characters'], ['characters.id'], name='favorites_favorite_characters_fkey'),
    sa.ForeignKeyConstraint(['favorite_planets'], ['planets.id'], name='favorites_favorite_planets_fkey'),
    sa.ForeignKeyConstraint(['related_user'], ['user.id'], name='favorites_related_user_fkey'),
    sa.PrimaryKeyConstraint('id', name='favorites_pkey')
    )
    op.drop_table('favorite_planets')
    op.drop_table('favorite_characters')
    # ### end Alembic commands ###