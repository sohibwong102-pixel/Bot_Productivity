# states/tool_states.py
from aiogram.fsm.state import State, StatesGroup

class ToolStates(StatesGroup):
    """
    FSM State sederhana untuk menangani input dari user secara terarah.
    """
    waiting_for_input = State()  # State ketika bot menunggu kiriman teks dari user
