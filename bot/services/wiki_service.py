import wikipediaapi


def get_wiki_instance(language):
    return wikipediaapi.Wikipedia(
        user_agent='MyProjectName (merlin@example.com)',
        language=language,
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )
