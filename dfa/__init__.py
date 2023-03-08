from blagues_api import BlaguesAPI
from dotenv import load_dotenv

load_dotenv()

const blagues = BlaguesAPI(BLAGUESAPI)

const blague = await blagues.random()

print(const blague)