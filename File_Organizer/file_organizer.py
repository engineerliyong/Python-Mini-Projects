import os
import shutil
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class FileOrganizer:
    # Extension to folder mapping
    CATEGORIES = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.md'],
        'Spreadsheets': ['.xls', '.xlsx', '.csv', '.ods'],
        'Presentations': ['.ppt', '.pptx', '.odp'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
        'Video': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java', '.php', '.json', '.xml'],
        'Executables': ['.exe', '.msi', '.app', '.deb', '.rpm'],
        'Others': []  # Default category for unrecognized extensions
    }
    
    def __init__(self, directory):
        self.directory = Path(directory).resolve()
        self.undo_history = []
        self.history_file = self.directory / '.organizer_history.json'
        self.load_history()
    
    def scan_directory(self):
        """List all files in the directory (excluding organizer folders)"""
        files = []
        for item in self.directory.iterdir():
            if item.is_file() and not item.name.startswith('.organizer'):
                files.append(item)
        return files
    
    def categorize_file(self, file_path):
        """Categorize a file based on its extension"""
        ext = file_path.suffix.lower()
        
        for category, extensions in self.CATEGORIES.items():
            if ext in extensions:
                return category
        return 'Others'
    
    def create_category_folders(self):
        """Create all category folders if they don't exist"""
        created_folders = []
        for category in self.CATEGORIES.keys():
            folder_path = self.directory / category
            if not folder_path.exists():
                folder_path.mkdir(exist_ok=True)
                created_folders.append(category)
        return created_folders
    
    def get_unique_filename(self, target_path):
        """Generate a unique filename if file already exists"""
        if not target_path.exists():
            return target_path
        
        counter = 1
        stem = target_path.stem
        suffix = target_path.suffix
        parent = target_path.parent
        
        while True:
            new_name = f"{stem}_{counter}{suffix}"
            new_path = parent / new_name
            if not new_path.exists():
                return new_path
            counter += 1
    
    def move_file(self, file_path, category):
        """Move a file to its category folder"""
        folder_path = self.directory / category
        target_path = folder_path / file_path.name
        unique_target = self.get_unique_filename(target_path)
        
        # Record for undo
        self.undo_history.append({
            'original': str(file_path),
            'new': str(unique_target),
            'category': category,
            'timestamp': datetime.now().isoformat()
        })
        
        shutil.move(str(file_path), str(unique_target))
        return unique_target
    
    def organize(self, dry_run=False):
        """Main organize function"""
        print(f"\n{'='*50}")
        print(f"Organizing: {self.directory}")
        print(f"{'='*50}\n")
        
        # Scan directory
        files = self.scan_directory()
        
        if not files:
            print("No files found to organize.")
            return
        
        print(f"Found {len(files)} files to organize.\n")
        
        # Create category folders
        created = self.create_category_folders()
        if created and not dry_run:
            print(f"Created folders: {', '.join(created)}")
        
        # Group files by category
        categorized = defaultdict(list)
        for file in files:
            category = self.categorize_file(file)
            categorized[category].append(file)
        
        # Display plan
        print("\nOrganization Plan:")
        print("-" * 40)
        for category, file_list in categorized.items():
            print(f"\n{category} ({len(file_list)} files):")
            for file in file_list:
                print(f"  → {file.name}")
        
        if dry_run:
            print("\n[Dry Run] No files were actually moved.")
            return
        
        # Confirm with user
        response = input(f"\nProceed with organization? (yes/no): ").lower()
        if response != 'yes':
            print("Operation cancelled.")
            return
        
        # Move files
        moved_count = 0
        for category, file_list in categorized.items():
            for file in file_list:
                new_path = self.move_file(file, category)
                print(f"Moved: {file.name} → {category}/{new_path.name}")
                moved_count += 1
        
        # Save history
        self.save_history()
        
        print(f"\n✅ Successfully organized {moved_count} files!")
        print(f"💡 Use 'undo' to restore original structure.")
    
    def save_history(self):
        """Save undo history to file"""
        with open(self.history_file, 'w') as f:
            json.dump(self.undo_history, f, indent=2)
    
    def load_history(self):
        """Load undo history from file"""
        if self.history_file.exists():
            try:
                with open(self.history_file, 'r') as f:
                    self.undo_history = json.load(f)
            except:
                self.undo_history = []
        else:
            self.undo_history = []
    
    def undo_last_operation(self):
        """Undo the last organize operation"""
        if not self.undo_history:
            print("No organization history found to undo.")
            return False
        
        print(f"\n{'='*50}")
        print("UNDO OPERATION")
        print(f"{'='*50}\n")
        
        # Group by timestamp (operation)
        operations = {}
        for record in self.undo_history:
            timestamp = record['timestamp']
            if timestamp not in operations:
                operations[timestamp] = []
            operations[timestamp].append(record)
        
        last_timestamp = max(operations.keys())
        last_operation = operations[last_timestamp]
        
        print(f"Undoing operation from: {last_timestamp}")
        print(f"Files to restore: {len(last_operation)}\n")
        
        response = input(f"Undo this operation? (yes/no): ").lower()
        if response != 'yes':
            print("Undo cancelled.")
            return False
        
        # Restore files
        restored = 0
        for record in reversed(last_operation):
            original = Path(record['original'])
            current = Path(record['new'])
            
            if not current.exists():
                print(f"⚠️  Warning: {current.name} no longer exists, skipping...")
                continue
            
            # Create original parent directory if needed
            original.parent.mkdir(parents=True, exist_ok=True)
            
            # Handle conflicts
            if original.exists():
                original = self.get_unique_filename(original)
                print(f"Note: {original.name} already exists, saving as {original.name}")
            
            shutil.move(str(current), str(original))
            print(f"Restored: {current.name} → {original.parent.name}/")
            restored += 1
        
        # Remove undone records from history
        self.undo_history = [r for r in self.undo_history 
                           if r['timestamp'] != last_timestamp]
        self.save_history()
        
        print(f"\n✅ Successfully restored {restored} files!")
        return True
    
    def show_stats(self):
        """Display statistics about the organized files"""
        files = self.scan_directory()
        if not files:
            print("No files found in current directory structure.")
            return
        
        stats = defaultdict(list)
        for file in files:
            category = self.categorize_file(file)
            stats[category].append(file)
        
        print(f"\n{'='*50}")
        print("ORGANIZATION STATISTICS")
        print(f"{'='*50}\n")
        
        total_files = sum(len(files) for files in stats.values())
        print(f"Total files organized: {total_files}")
        print(f"Categories used: {len(stats)}\n")
        
        for category, file_list in sorted(stats.items()):
            size_bytes = sum(f.stat().st_size for f in file_list)
            size_mb = size_bytes / (1024 * 1024)
            print(f"{category}: {len(file_list)} files ({size_mb:.2f} MB)")


def main():
    print("\n" + "="*50)
    print("📁 FILE ORGANIZER")
    print("="*50)
    
    while True:
        print("\nOptions:")
        print("1. Organize files")
        print("2. Show current statistics")
        print("3. Undo last operation")
        print("4. Change directory")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == '1':
            directory = input("Enter directory path to organize: ").strip()
            if not directory:
                print("Invalid directory path.")
                continue
            
            if not os.path.exists(directory):
                print("Directory does not exist!")
                continue
            
            organizer = FileOrganizer(directory)
            dry_run = input("Run dry run first? (yes/no): ").lower() == 'yes'
            organizer.organize(dry_run=dry_run)
        
        elif choice == '2':
            directory = input("Enter directory path: ").strip()
            if not directory or not os.path.exists(directory):
                print("Invalid directory path!")
                continue
            organizer = FileOrganizer(directory)
            organizer.show_stats()
        
        elif choice == '3':
            directory = input("Enter the organized directory path: ").strip()
            if not directory or not os.path.exists(directory):
                print("Invalid directory path!")
                continue
            organizer = FileOrganizer(directory)
            organizer.undo_last_operation()
        
        elif choice == '4':
            print("Directory will be changed in next operation.")
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()