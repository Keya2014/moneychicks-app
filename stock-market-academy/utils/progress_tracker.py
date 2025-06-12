class ProgressTracker:
    def __init__(self):
        self.completed = set()
    
    def mark_completed(self, module):
        self.completed.add(module)
    
    def is_completed(self, module):
        return module in self.completed
    
    def get_overall_progress(self):
        # Example: 7 modules in total
        return (len(self.completed) / 7) * 100
