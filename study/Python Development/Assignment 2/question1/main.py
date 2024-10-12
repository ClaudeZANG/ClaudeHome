def read_world_series_winners(file_name):
    try:
        # 打开文件并读取内容
        with open(file_name, 'r') as file:
            winners = [line.strip() for line in file] # 读取文件的所有行

        winner_counts = {}

        # 遍历文件中的每个队伍名并进行统计
        for winner in winners:
            if winner in winner_counts:
                winner_counts[winner] += 1  # 如果队伍已存在字典中，增加计数
            else:
                winner_counts[winner] = 1  # 如果队伍第一次出现，初始化计数为 1

        return winner_counts

    except FileNotFoundError:
        print(f"Error: The file {file_name} does not exist.")
        return None

def query_team_wins(winner_counts):
    if winner_counts is None:
        return

    # 提示用户输入队伍名称
    team = input("Enter the name of the team: ")

    # 查询队伍的获胜次数
    if team in winner_counts:
        print(f"The {team} won the World Series {winner_counts[team]} times.")
    else:
        print(f"The {team} did not win the World Series during the period from 1903 to 2019.")

def main():
    file_name = 'WorldSeriesWinners.txt'  # 文件名
    winner_counts = read_world_series_winners(file_name)  # 读取文件并统计获胜次数
    query_team_wins(winner_counts)  # 进行查询

if __name__ == "__main__":
    main()
