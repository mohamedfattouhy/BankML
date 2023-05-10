from enum import Enum


class EducationLevel(str, Enum):
    primary = "primary"
    secondary = "secondary"
    tertiary = "tertiary"


class Marital(str, Enum):
    divorced = "divorced"
    married = "married"
    single = "single"


class Default(str, Enum):
    yes = "yes"
    no = "no"


class Loan(str, Enum):
    yes = "yes"
    no = "no"


class Housing(str, Enum):
    yes = "yes"
    no = "no"


class Job(str, Enum):
    management = "management"
    services = "services"
    admin = "admin."
    blue_collar = "blue-collar"
    entrepreneur = "entrepreneur"
    housemaid = "housemaid"
    student = "student"
    unemployed = "unemployed"
    technician = "technician"
    retired = "retired"
    self_employed = "self-employed"
    unknown = "unknown"


class Contact(str, Enum):
    cellular = "cellular"
    telephone = "telephone"
    unknown = "unknown"


class Poutcoume(str, Enum):
    success = "success"
    failure = "failure"
    other = "other"
    unknown = "unknown"


class Month(str, Enum):
    jan = "jan"
    feb = "feb"
    mar = "mar"
    apr = "apr"
    may = "may"
    jun = "jun"
    jul = "jul"
    aug = "aug"
    sep = "sep"
    oct = "oct"
    nov = "nov"
    dec = "dec"
