from rich import print
class ToDoList:
    def __init__(self):
        self.all_tasks = {} 

    def add_task(self, description):
        self.all_tasks[len(self.all_tasks) + 1] = {'description': description, 'completed': False}
        print('\n[bright_blue][bold]Successfully Added.[/bright_blue][/bold]')

    def mark_task_as_completed(self, task_number):
        if task_number in self.all_tasks:
            self.all_tasks[task_number]['completed'] = True
            print(f'\n[bright_blue]Task {task_number} marked as completed.[/bright_blue]')
        else:
            print('\n[bright_red][bold]Task number not found.[/bright_red][/bold]')

    def view_tasks(self):
        if self.all_tasks:
            print("\n[green][bold]To-Do List:-[/bold][/green]\n")
            for task_number, task in self.all_tasks.items():
                status = 'Completed' if task['completed'] else 'Incomplete'
                print(f"{task_number}.[dark_red] {task['description']} [/dark_red] - [bright_yellow]{status}[/bright_yellow]")
        else:
            print("\n[bright_red][bold]No tasks found.[/bright_red][/bold]")

def main():
    todo_list = ToDoList() 
    
    while True:
        print("\n_____________________________")
        print("\n[bold][green]Choose the following options:\n[green][/bold]")
        print("1.[blue_violet] Add Task [/blue_violet]")
        print("2.[chartreuse2] Mark Task as Completed[/chartreuse2]")
        print("3.[gold3] View Tasks [/gold3]")
        print("4.[deep_pink3] Exit [/deep_pink3]")
        print("_____________________________\n")
        print("[bold][purple4]Enter your choice:[/purple4][/bold]")
        choice = input()
            
        if choice == '1':
           
            print("\n[bold][bright_green]Task description:-[/bright_green][/bold]\n")
            description = input()
            todo_list.add_task(description)
                
        elif choice == '2':
            print("\n[green][bold]Enter task number: [/bold][/green]")
            task_number = int(input())
            todo_list.mark_task_as_completed(task_number)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("\n[bright_red][bold]Exiting program.[/bold][/bright_red]")
            break
        else:
            print("\n[bright_red][bold]Invalid choice. Please try again.[/bold][/bright_red]")

if __name__ == "__main__":
    main()