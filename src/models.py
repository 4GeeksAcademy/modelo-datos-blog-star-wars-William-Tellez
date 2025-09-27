from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column
import datetime

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(80), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    create_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)
    is_active: Mapped[bool] = mapped_column(Boolean(), default=True, nullable=False)
    favoritos = db.relationship('Favorito')

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "last_name": self.last_name,
            "create_at": self.create_at.isoformat(),
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }
class Personaje(db.Model):
    __tablename__ = "personaje"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    gender: Mapped[str] = mapped_column(String(20), nullable=True)
    birth_year: Mapped[str] = mapped_column(String(20), nullable=True)
    height: Mapped[str] = mapped_column(String(10), nullable=True)
    mass: Mapped[str] = mapped_column(String(10), nullable=True)
    hair_color: Mapped[str] = mapped_column(String(30), nullable=True)
    skin_color: Mapped[str] = mapped_column(String(30), nullable=True)
    eye_color: Mapped[str] = mapped_column(String(30), nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)
    favoritos = db.relationship('Favorito')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birth_year": self.birth_year,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }

class Planeta(db.Model):
    __tablename__ = "planeta"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    climate: Mapped[str] = mapped_column(nullable=True)
    diameter: Mapped[int] = mapped_column(nullable=True)
    gravity: Mapped[str] = mapped_column(nullable=True)
    population: Mapped[int] = mapped_column(nullable=True)
    terrain: Mapped[str] = mapped_column(nullable=True)
    rotation_period: Mapped[int] = mapped_column(nullable=True)
    orbital_period: Mapped[int] = mapped_column(nullable=True)
    surface_water: Mapped[int] = mapped_column(nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)
    favoritos = db.relationship('Favorito')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "population": self.population,
            "terrain": self.terrain,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "surface_water": self.surface_water,
            "created_at": self.created_at
        }

class Favorito(db.Model):
    __tablename__ = "favoritos"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"), nullable=False)
    personaje_id: Mapped[int] = mapped_column(db.ForeignKey("personaje.id"), nullable=True)
    planeta_id: Mapped[int] = mapped_column(db.ForeignKey("planeta.id"), nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "personaje_id": self.personaje_id,
            "planeta_id": self.planeta_id,
            "created_at": self.created_at
        }

    
