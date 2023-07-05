from datetime import date, timedelta
from data import DataSet
from crawler import Cohort, Tournament

# Initiate dataset object
data = DataSet()

# Constants
POST_CODE = 'WV11+8PP'
DISTANCE = 50
DAYS = 28
START_DATE = date.today().strftime("%Y-%m-%d")
END_DATE = (date.today() + timedelta(days=DAYS)).strftime("%Y-%m-%d")
COHORT_LINKS = {'11U GS': f"https://competitions.lta.org.uk/find?DateFilterType=0&StartDate={START_DATE}&EndDate={END_DATE}&LocationFilterType=0&PostalCode={POST_CODE}&Distance={DISTANCE}&TournamentCategoryIDList%5B0%5D=26&TournamentCategoryIDList%5B1%5D=24&TournamentCategoryIDList%5B2%5D=33&TournamentCategoryIDList%5B3%5D=23&TournamentCategoryIDList%5B4%5D=false&TournamentCategoryIDList%5B5%5D=18&TournamentCategoryIDList%5B6%5D=19&TournamentCategoryIDList%5B7%5D=false&TournamentCategoryIDList%5B8%5D=false&TournamentCategoryIDList%5B9%5D=false&TournamentCategoryIDList%5B10%5D=2&TournamentCategoryIDList%5B11%5D=34&AgeGroupIDList%5B0%5D=false&AgeGroupIDList%5B1%5D=false&AgeGroupIDList%5B2%5D=false&AgeGroupIDList%5B3%5D=11&AgeGroupIDList%5B4%5D=false&AgeGroupIDList%5B5%5D=false&AgeGroupIDList%5B6%5D=false&AgeGroupIDList%5B7%5D=false&AgeGroupIDList%5B8%5D=false&AgeGroupIDList%5B9%5D=false&AgeGroupIDList%5B10%5D=false&AgeGroupIDList%5B11%5D=false&AgeGroupIDList%5B12%5D=false&AgeGroupIDList%5B13%5D=false&AgeGroupIDList%5B14%5D=false&AgeGroupIDList%5B15%5D=false&AgeGroupIDList%5B16%5D=false&AgeGroupIDList%5B17%5D=false&AgeGroupIDList%5B18%5D=false&AgeGroupIDList%5B19%5D=false&AgeGroupIDList%5B20%5D=false&AgeGroupIDList%5B21%5D=false&page=1&EventGameTypeIDList%5B0%5D=false&EventGameTypeIDList%5B1%5D=2&EventGameTypeIDList%5B2%5D=false&EventGameTypeIDList%5B3%5D=false&EventGameTypeIDList%5B4%5D=false&EventGameTypeIDList%5B5%5D=false&EventGameTypeIDList%5B6%5D=false&GradingIDList%5B0%5D=false&GradingIDList%5B1%5D=false&GradingIDList%5B2%5D=3&GradingIDList%5B3%5D=4&GradingIDList%5B4%5D=5&GradingIDList%5B5%5D=false&GradingIDList%5B6%5D=false&GradingIDList%5B7%5D=false",
                '11U GD': f"https://competitions.lta.org.uk/find?DateFilterType=0&StartDate={START_DATE}&EndDate={END_DATE}&LocationFilterType=0&PostalCode={POST_CODE}&Distance={DISTANCE}&TournamentCategoryIDList%5B0%5D=26&TournamentCategoryIDList%5B1%5D=24&TournamentCategoryIDList%5B2%5D=33&TournamentCategoryIDList%5B3%5D=23&TournamentCategoryIDList%5B4%5D=false&TournamentCategoryIDList%5B5%5D=18&TournamentCategoryIDList%5B6%5D=19&TournamentCategoryIDList%5B7%5D=false&TournamentCategoryIDList%5B8%5D=false&TournamentCategoryIDList%5B9%5D=false&TournamentCategoryIDList%5B10%5D=2&TournamentCategoryIDList%5B11%5D=34&AgeGroupIDList%5B0%5D=false&AgeGroupIDList%5B1%5D=false&AgeGroupIDList%5B2%5D=false&AgeGroupIDList%5B3%5D=11&AgeGroupIDList%5B4%5D=false&AgeGroupIDList%5B5%5D=false&AgeGroupIDList%5B6%5D=false&AgeGroupIDList%5B7%5D=false&AgeGroupIDList%5B8%5D=false&AgeGroupIDList%5B9%5D=false&AgeGroupIDList%5B10%5D=false&AgeGroupIDList%5B11%5D=false&AgeGroupIDList%5B12%5D=false&AgeGroupIDList%5B13%5D=false&AgeGroupIDList%5B14%5D=false&AgeGroupIDList%5B15%5D=false&AgeGroupIDList%5B16%5D=false&AgeGroupIDList%5B17%5D=false&AgeGroupIDList%5B18%5D=false&AgeGroupIDList%5B19%5D=false&AgeGroupIDList%5B20%5D=false&AgeGroupIDList%5B21%5D=false&page=1&EventGameTypeIDList%5B0%5D=false&EventGameTypeIDList%5B1%5D=false&EventGameTypeIDList%5B2%5D=false&EventGameTypeIDList%5B3%5D=4&EventGameTypeIDList%5B4%5D=false&EventGameTypeIDList%5B5%5D=false&EventGameTypeIDList%5B6%5D=false&GradingIDList%5B0%5D=false&GradingIDList%5B1%5D=false&GradingIDList%5B2%5D=3&GradingIDList%5B3%5D=4&GradingIDList%5B4%5D=5&GradingIDList%5B5%5D=false&GradingIDList%5B6%5D=false&GradingIDList%5B7%5D=false",
                '12U GS': f"https://competitions.lta.org.uk/find?DateFilterType=0&StartDate={START_DATE}&EndDate={END_DATE}&LocationFilterType=0&PostalCode={POST_CODE}&Distance={DISTANCE}&TournamentCategoryIDList%5B0%5D=26&TournamentCategoryIDList%5B1%5D=24&TournamentCategoryIDList%5B2%5D=33&TournamentCategoryIDList%5B3%5D=23&TournamentCategoryIDList%5B4%5D=false&TournamentCategoryIDList%5B5%5D=18&TournamentCategoryIDList%5B6%5D=19&TournamentCategoryIDList%5B7%5D=false&TournamentCategoryIDList%5B8%5D=false&TournamentCategoryIDList%5B9%5D=false&TournamentCategoryIDList%5B10%5D=2&TournamentCategoryIDList%5B11%5D=34&AgeGroupIDList%5B0%5D=false&AgeGroupIDList%5B1%5D=false&AgeGroupIDList%5B2%5D=false&AgeGroupIDList%5B3%5D=false&AgeGroupIDList%5B4%5D=12&AgeGroupIDList%5B5%5D=false&AgeGroupIDList%5B6%5D=false&AgeGroupIDList%5B7%5D=false&AgeGroupIDList%5B8%5D=false&AgeGroupIDList%5B9%5D=false&AgeGroupIDList%5B10%5D=false&AgeGroupIDList%5B11%5D=false&AgeGroupIDList%5B12%5D=false&AgeGroupIDList%5B13%5D=false&AgeGroupIDList%5B14%5D=false&AgeGroupIDList%5B15%5D=false&AgeGroupIDList%5B16%5D=false&AgeGroupIDList%5B17%5D=false&AgeGroupIDList%5B18%5D=false&AgeGroupIDList%5B19%5D=false&AgeGroupIDList%5B20%5D=false&AgeGroupIDList%5B21%5D=false&page=1&EventGameTypeIDList%5B0%5D=false&EventGameTypeIDList%5B1%5D=2&EventGameTypeIDList%5B2%5D=false&EventGameTypeIDList%5B3%5D=false&EventGameTypeIDList%5B4%5D=false&EventGameTypeIDList%5B5%5D=false&EventGameTypeIDList%5B6%5D=false&GradingIDList%5B0%5D=false&GradingIDList%5B1%5D=false&GradingIDList%5B2%5D=3&GradingIDList%5B3%5D=4&GradingIDList%5B4%5D=5&GradingIDList%5B5%5D=false&GradingIDList%5B6%5D=false&GradingIDList%5B7%5D=false",
                '14U GS': f"https://competitions.lta.org.uk/find?DateFilterType=0&StartDate={START_DATE}&EndDate={END_DATE}&LocationFilterType=0&PostalCode={POST_CODE}&Distance={DISTANCE}&TournamentCategoryIDList%5B0%5D=26&TournamentCategoryIDList%5B1%5D=24&TournamentCategoryIDList%5B2%5D=33&TournamentCategoryIDList%5B3%5D=23&TournamentCategoryIDList%5B4%5D=false&TournamentCategoryIDList%5B5%5D=18&TournamentCategoryIDList%5B6%5D=19&TournamentCategoryIDList%5B7%5D=false&TournamentCategoryIDList%5B8%5D=false&TournamentCategoryIDList%5B9%5D=false&TournamentCategoryIDList%5B10%5D=2&TournamentCategoryIDList%5B11%5D=34&AgeGroupIDList%5B0%5D=false&AgeGroupIDList%5B1%5D=false&AgeGroupIDList%5B2%5D=false&AgeGroupIDList%5B3%5D=false&AgeGroupIDList%5B4%5D=false&AgeGroupIDList%5B5%5D=14&AgeGroupIDList%5B6%5D=false&AgeGroupIDList%5B7%5D=false&AgeGroupIDList%5B8%5D=false&AgeGroupIDList%5B9%5D=false&AgeGroupIDList%5B10%5D=false&AgeGroupIDList%5B11%5D=false&AgeGroupIDList%5B12%5D=false&AgeGroupIDList%5B13%5D=false&AgeGroupIDList%5B14%5D=false&AgeGroupIDList%5B15%5D=false&AgeGroupIDList%5B16%5D=false&AgeGroupIDList%5B17%5D=false&AgeGroupIDList%5B18%5D=false&AgeGroupIDList%5B19%5D=false&AgeGroupIDList%5B20%5D=false&AgeGroupIDList%5B21%5D=false&page=1&EventGameTypeIDList%5B0%5D=false&EventGameTypeIDList%5B1%5D=2&EventGameTypeIDList%5B2%5D=false&EventGameTypeIDList%5B3%5D=false&EventGameTypeIDList%5B4%5D=false&EventGameTypeIDList%5B5%5D=false&EventGameTypeIDList%5B6%5D=false&GradingIDList%5B0%5D=false&GradingIDList%5B1%5D=false&GradingIDList%5B2%5D=3&GradingIDList%5B3%5D=4&GradingIDList%5B4%5D=5&GradingIDList%5B5%5D=false&GradingIDList%5B6%5D=false&GradingIDList%5B7%5D=false"}


def main():
    # Find tournaments for each of the cohorts
    print(f"{len(COHORT_LINKS)} cohorts found . Crawling cohort data...")
    for cohort, weblink in COHORT_LINKS.items():
        cohorts = Cohort()
        tournaments = cohorts.crawl_cohort(cohort, weblink)

        # Find tournament data for each of the tournaments
        print(f"{len(tournaments)} tournaments found in cohort {cohort}. Crawling tournament data...")
        for tournament in tournaments:
            crawl = Tournament(tournament, cohort)
            tournament_data = crawl.crawl_tournament()
            data.insert_data(tournament_data)

    # Send data to google sheet
    data.export_google()


if __name__ == "__main__":
    main()
