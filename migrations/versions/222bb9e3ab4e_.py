"""empty message

Revision ID: 222bb9e3ab4e
Revises: 
Create Date: 2020-05-09 23:56:12.154234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '222bb9e3ab4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('first_name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('skype', sa.String(length=35), nullable=True),
    sa.Column('address_1', sa.String(length=120), nullable=True),
    sa.Column('address_2', sa.String(length=120), nullable=True),
    sa.Column('address_3', sa.String(length=120), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('country', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('zipcode', sa.String(length=5), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='true', nullable=True),
    sa.Column('last_login_at', sa.DateTime(), nullable=True),
    sa.Column('registered_at', sa.DateTime(), nullable=True),
    sa.Column('roles', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
