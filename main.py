import animator
import pathfinder
import yaml

if __name__ == "__main__":
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        
        update_time = config['update_time']
        animation = config['animation']
        maze_algorithm = config['algorithms']['maze']
        path_algorithm = config['algorithms']['path']
        width = config['dimensions']['width']
        height = config['dimensions']['height']
        ascii_maze = config['ascii']['maze']
        ascii_path = config['ascii']['path']

        ascii_maze = config['ascii_sets'][ascii_maze]
        ascii_path = config['ascii_sets'][ascii_path]

    if animation:
        animator.main(update_time, maze_algorithm, path_algorithm, width, height, ascii_maze, ascii_path)
    else:
        pathfinder.main(maze_algorithm=maze_algorithm, 
                        path_algorithm=path_algorithm, 
                        width=width, 
                        height=height, 
                        ascii_maze=ascii_maze, 
                        ascii_path=ascii_path,
                        print_path=True)

