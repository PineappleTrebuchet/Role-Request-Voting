from dataclasses import dataclass

DEFAULT_VOTE = 1


@dataclass(frozen=True)
class Role:
    name: str  # Name of the role
    votes: int  # Vote weight (number of votes they can cast)
    percent_accept: float  # Percentage of votes needed to approve a request for this role
    can_be_voted_on: bool = True # If true, this role can be voted on
    ignore_vote_weight: bool = False # If true, requests for this role will ignore the vote weight of other roles voting on it
    command_whitelisted: bool = False  # If true, this role can use restricted commands


ROLES = [
    Role(
        name="Excelsior",
        votes=DEFAULT_VOTE,
        percent_accept=0.0,
        can_be_voted_on=False,
        ignore_vote_weight=False,
        command_whitelisted=False,
    ),
    Role(
        name="Adept",
        votes=2,
        percent_accept=0.5,
    ),
    Role(
        name="Expert",
        votes=3,
        percent_accept=0.75,
    ),
    Role(
        name="Paragon",
        votes=4,
        percent_accept=0.9,
        command_whitelisted=True,
    ),
    Role(
        name="Artisan",
        votes=DEFAULT_VOTE,
        percent_accept=0.66,
        ignore_vote_weight=True,
    ),
    Role(
        name="Visionary",
        votes=DEFAULT_VOTE,
        percent_accept=0.75,
    ),
    Role(
        name="Custodian (admin)",
        votes=DEFAULT_VOTE,
        percent_accept=0.0,
        can_be_voted_on=False,
        command_whitelisted=True,
    ),
    Role(
        name="Sentinel (mod)",
        votes=DEFAULT_VOTE,
        percent_accept=0.0,
        can_be_voted_on=False,
        command_whitelisted=True,
    ),
    Role(
        name="Bot Manager",
        votes=DEFAULT_VOTE,
        percent_accept=0.0,
        can_be_voted_on=False,
        command_whitelisted=True,
    ),
]


# Role to vote count mapping
ROLE_VOTES = {role.name: role.votes for role in ROLES}

# Roles that can use restricted commands
COMMAND_WHITELISTED_ROLES = [role.name for role in ROLES if role.command_whitelisted]

# Roles to be voted on
VALID_ROLES = [role.name for role in ROLES if role.can_be_voted_on]

# Role acceptance thresholds (as a percentage)
ACCEPTANCE_THRESHOLDS = {role.name: role.percent_accept for role in ROLES if role.can_be_voted_on}

# Roles that ignore the vote weight of other roles
IGNORE_VOTE_WEIGHT = [role.name for role in ROLES if role.ignore_vote_weight and role.can_be_voted_on]

# Thread tags (incase you have different names for your tags)
THREAD_TAGS = {"Approved": "Approved", "Denied": "Denied"}


VOTE_TIME_PERIOD = (60 * 60 * 24 * 7)  # 7 days in seconds
CHECK_TIME = 60  # how often you want to check if the voting period has ended; in seconds
CLOSE_POST = False  # if true, the bot will close the post after the voting period ends

# Vote feedback
PROMPT_NO_VOTERS_FOR_FEEDBACK = True # whether to prompt people voting 'no' for feedback
PROMPT_YES_VOTERS_FOR_FEEDBACK = True # whether to prompt people voting 'yes' for feedback
PROMPT_AFTER_FIRST_FEEDBACK = True # whether to only prompt people until someone submits feedback, or keep prompting everyone

CHANNEL_ID = 1101149194498089051  # Forum channel ID
MOD_LOG_CHANNEL_ID = 546319957827518474  # Channel for moderation logs
STATE_FILE_NAME = "requests_state.json"
LOG_FILE_NAME = "requests_log.txt"
DEV_MODE = False  # for ease of testing, turns off many checks
