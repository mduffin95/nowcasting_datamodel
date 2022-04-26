"""empty message

Revision ID: f4bb5237f428
Revises: d2f031f24593
Create Date: 2022-04-26 11:49:37.117564

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "f4bb5237f428"
down_revision = "d2f031f24593"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        op.f("ix_forecast_value_target_time"), "forecast_value", ["target_time"], unique=False
    )
    op.create_index(op.f("ix_location_gsp_id"), "location", ["gsp_id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_location_gsp_id"), table_name="location")
    op.drop_index(op.f("ix_forecast_value_target_time"), table_name="forecast_value")
    # ### end Alembic commands ###
