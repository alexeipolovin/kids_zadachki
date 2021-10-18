def snake_case_split(identifier):
    return ' '.join(identifier.split("_"))


def self_destroy(identifier, splitter):
    return ' '.join(identifier.split(splitter))
