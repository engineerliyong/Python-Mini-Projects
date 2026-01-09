"""
File Word Counter
Original by: Liza Bambu
Enhanced: January 2026

Analyzes text files for word frequency and generates detailed reports.
"""

from collections import Counter
import string


def count_words(file_path):
    """
    Counts the number of words in a text file.
    
    Args:
        file_path (str): Path to the text file.
    
    Returns:
        int: Total number of words in the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()  # Split by whitespace
            return len(words)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0


def clean_text(text):
    """
    Clean text by removing punctuation and converting to lowercase.
    
    Args:
        text (str): Raw text to clean
        
    Returns:
        str: Cleaned text
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    return text


def analyze_file(file_path):
    """
    Perform comprehensive word frequency analysis on a text file.
    
    Args:
        file_path (str): Path to the text file.
    
    Returns:
        dict: Analysis results including total words, unique words, and frequencies.
              Returns None if file cannot be read.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            
            # Clean the text
            cleaned_text = clean_text(text)
            
            # Split into words
            words = cleaned_text.split()
            
            # Count total words
            total_words = len(words)
            
            # Count word frequencies
            word_frequencies = Counter(words)
            
            # Get unique word count
            unique_words = len(word_frequencies)
            
            # Get most common words (top 10)
            most_common = word_frequencies.most_common(10)
            
            # Build results dictionary
            results = {
                'total_words': total_words,
                'unique_words': unique_words,
                'most_common': most_common,
                'all_frequencies': word_frequencies
            }
            
            return results
            
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def display_results(results):
    """
    Display analysis results in a formatted way.
    
    Args:
        results (dict): Analysis results from analyze_file()
    """
    if results is None:
        return
    
    print("\n" + "=" * 60)
    print("  WORD FREQUENCY ANALYSIS")
    print("=" * 60)
    print(f"\nTotal words: {results['total_words']:,}")
    print(f"Unique words: {results['unique_words']:,}")
    
    print("\n" + "-" * 60)
    print("Top 10 Most Common Words:")
    print("-" * 60)
    
    for rank, (word, count) in enumerate(results['most_common'], 1):
        # Calculate percentage
        percentage = (count / results['total_words']) * 100
        print(f"  {rank:2d}. {word:15s} : {count:4d} times ({percentage:5.2f}%)")
    
    print()


def save_report(results, output_file):
    """
    Save analysis results to a text file.
    
    Args:
        results (dict): Analysis results from analyze_file()
        output_file (str): Path to the output file
    """
    if results is None:
        return
    
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("=" * 60 + "\n")
            file.write("  WORD FREQUENCY ANALYSIS REPORT\n")
            file.write("=" * 60 + "\n\n")
            
            file.write(f"Total words: {results['total_words']:,}\n")
            file.write(f"Unique words: {results['unique_words']:,}\n\n")
            
            file.write("-" * 60 + "\n")
            file.write("Top 10 Most Common Words:\n")
            file.write("-" * 60 + "\n")
            
            for rank, (word, count) in enumerate(results['most_common'], 1):
                percentage = (count / results['total_words']) * 100
                file.write(f"  {rank:2d}. {word:15s} : {count:4d} times ({percentage:5.2f}%)\n")
            
            file.write("\n" + "=" * 60 + "\n")
            file.write("Full Word List (sorted by frequency):\n")
            file.write("=" * 60 + "\n")
            
            # Write all words sorted by frequency
            for word, count in results['all_frequencies'].most_common():
                file.write(f"{word:20s} : {count:4d}\n")
        
        print(f"✓ Report saved successfully to: {output_file}")
        
    except Exception as e:
        print(f"Error saving report: {e}")


if __name__ == "__main__":
    print("=" * 60)
    print("  FILE WORD COUNTER")
    print("=" * 60)
    print()
    
    # Get file path from user
    file_path = input("Enter the path to your text file: ")
    
    # Analyze the file
    results = analyze_file(file_path)
    
    if results:
        # Display results
        display_results(results)
        
        # Ask if user wants to save report
        save_choice = input("Would you like to save the report to a file? (y/n): ").lower()
        
        if save_choice == 'y':
            output_file = input("Enter output filename [report.txt]: ").strip()
            if not output_file:
                output_file = "report.txt"
            
            save_report(results, output_file)
        
        print("\nAnalysis complete! ✓")
    else:
        print("\nAnalysis failed. Please check the file path and try again.")