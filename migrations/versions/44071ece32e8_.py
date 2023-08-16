"""empty message

Revision ID: 44071ece32e8
Revises: 
Create Date: 2023-08-16 03:56:27.382184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44071ece32e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_name', sa.String(), nullable=False),
    sa.Column('character_gender', sa.String(), nullable=False),
    sa.Column('character_height', sa.String(), nullable=False),
    sa.Column('character_mass', sa.String(), nullable=False),
    sa.Column('character_hair_color', sa.String(), nullable=False),
    sa.Column('character_skin_color', sa.String(), nullable=False),
    sa.Column('character_eye_color', sa.String(), nullable=False),
    sa.Column('character_birth_year', sa.String(), nullable=False),
    sa.Column('character_home_world', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_name', sa.String(), nullable=False),
    sa.Column('rotation_period', sa.Integer(), nullable=False),
    sa.Column('orbital_period', sa.Integer(), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(), nullable=False),
    sa.Column('gravity', sa.Integer(), nullable=False),
    sa.Column('terrain', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('related_user', sa.Integer(), nullable=False),
    sa.Column('favorite_characters', sa.Integer(), nullable=False),
    sa.Column('favorite_planets', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['favorite_characters'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['favorite_planets'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['related_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('user')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###
