from datetime import datetime
from sqlalchemy import Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class PrepMaterial(Base):
    
    __tablename__ = "prep_materials"


    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    interview_id: Mapped[int] = mapped_column(
        ForeignKey("interviews.id")
    )

    technical_questions: Mapped[str] = mapped_column(
        Text
    )

    behavioral_questions: Mapped[str] = mapped_column(
        Text
    )

    study_plan: Mapped[str] = mapped_column(
        Text
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )