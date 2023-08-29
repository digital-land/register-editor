import datetime
from typing import List, Optional

from sqlalchemy import ForeignKey, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.orm import Mapped, mapped_column, relationship

from application.extensions import db

dataset_field = db.Table(
    "dataset_field",
    db.Column("dataset", db.Text, db.ForeignKey("dataset.dataset")),
    db.Column("field", db.Text, db.ForeignKey("field.field")),
    db.PrimaryKeyConstraint("dataset", "field"),
)


class DateModel(db.Model):
    __abstract__ = True

    entry_date: Mapped[Optional[datetime.date]] = mapped_column(
        db.Date, default=db.func.current_date()
    )
    start_date: Mapped[Optional[datetime.date]] = mapped_column(db.Date)
    end_date: Mapped[Optional[datetime.date]] = mapped_column(db.Date)


class Dataset(DateModel):
    __tablename__ = "dataset"

    dataset: Mapped[str] = mapped_column(Text, primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)

    fields: Mapped[List["Field"]] = relationship(
        "Field",
        secondary=dataset_field,
        back_populates="datasets",
        order_by="Field.name",
    )

    entries: Mapped[List["Entry"]] = relationship("Entry", back_populates="dataset")

    def __repr__(self):
        return f"<Dataset(id={self.name}, name={self.name}, fields={self.fields})>"


class Entry(db.Model):
    __tablename__ = "entry"

    id: Mapped[int] = mapped_column(db.BigInteger, primary_key=True)
    dataset_id: Mapped[str] = mapped_column(
        Text, ForeignKey("dataset.dataset"), primary_key=True
    )
    dataset: Mapped["Dataset"] = relationship("Dataset", back_populates="entries")
    data: Mapped[dict] = mapped_column(MutableDict.as_mutable(JSONB), nullable=False)

    def __repr__(self):
        return f"<Entry(dataset={self.dataset.name}, id={self.id}, data={self.data}))>"


class Field(DateModel):
    __tablename__ = "field"

    field: Mapped[str] = mapped_column(Text, primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    datatype: Mapped[str] = mapped_column(Text, nullable=False)
    datasets: Mapped[List["Dataset"]] = relationship(
        "Dataset", secondary=dataset_field, back_populates="fields"
    )

    def __repr__(self):
        return f"<Field(name={self.name})>"
