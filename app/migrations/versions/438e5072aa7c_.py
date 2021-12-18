"""empty message

Revision ID: 438e5072aa7c
Revises: 07383bac1d0c
Create Date: 2021-11-21 15:00:25.592695

"""
from alembic import op #Alembic is a lightweight database 
                        #migration tool for usage with the SQLAlchemy Database Toolkit for Python.
import sqlalchemy as sa #The Python SQL Toolkit and Object Relational Mapper


# revision identifiers, used by Alembic.
revision = '438e5072aa7c'
down_revision = '07383bac1d0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reply',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('thread_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('message', sa.String(length=200), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['thread_id'], ['thread.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reply')
    # ### end Alembic commands ###