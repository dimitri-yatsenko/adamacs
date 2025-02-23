import datajoint as dj

schema = dj.schema()

@schema
class Lab(dj.Manual):
    definition = """
    lab             : varchar(24)     
    ---
    lab_name        : varchar(255)
    institution     : varchar(255)
    address         : varchar(255)
    time_zone       : varchar(64)
    """

@schema
class Protocol(dj.Manual):
    definition = """
    # protocol approved by some institutions like IACUC, IRB
    protocol                        : varchar(16)
    ---
    protocol_description=NULL         : varchar(255)
    """

@schema
class Line(dj.Manual):
    definition = """
    # protocol approved by some institutions like IACUC, IRB
    line                        : varchar(32)
    ---
    line_description=NULL         : varchar(255)
    target_phenotype=NULL         : varchar(255)
    is_active                   : boolean
    """

@schema
class Subject(dj.Manual):
    definition = """
    # Animal Subject
    # Our Animals are not uniquely identified by their ID
    # because different labs use different animal facilities.
    subject                 : varchar(32)
    -> Lab
    ---
    sex                     : enum('M', 'F', 'U')
    subject_birth_date      : date
    subject_description=''  : varchar(1024)
    -> Line
    """

@schema
class SubjectDeath(dj.Manual):
    definition = """
    -> Subject
    ---
    death_date      : date       # death date
    cull_method:    varchar(255)
    """

@schema
class User(dj.Lookup):
    definition = """
    user                : varchar(32)
    ---
    -> Lab
    """

@schema
class Project(dj.Lookup):
    definition = """
    project                 : varchar(32)
    ---
    project_description=''         : varchar(1024)
    """
