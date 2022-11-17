"""empty message

Revision ID: 4d245e892640
Revises: d4c688511bf9
Create Date: 2022-11-15 11:50:10.675940

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "4d245e892640"
down_revision = "d4c688511bf9"
branch_labels = None
depends_on = None


def upgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        "idx_forecast_value_last_seven_days_created_utc",
        "forecast_value_last_seven_days",
        ["created_utc"],
        unique=False,
    )
    op.create_index(
        "idx_forecast_value_last_seven_days_target_time",
        "forecast_value_last_seven_days",
        ["target_time"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        "idx_forecast_value_last_seven_days_target_time",
        table_name="forecast_value_last_seven_days",
    )
    op.drop_index(
        "idx_forecast_value_last_seven_days_created_utc",
        table_name="forecast_value_last_seven_days",
    )
    # ### end Alembic commands ###