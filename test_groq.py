"""
Quick test script for Groq API key
"""

from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_groq_api():
    """Test Groq API key"""
    
    # Get API key
    api_key = os.getenv('GROQ_API_KEY')
    
    if not api_key:
        print("❌ ERROR: GROQ_API_KEY not found in .env file!")
        return False
    
    print(f"✓ API Key found: {api_key[:20]}...")
    print("\nTesting Groq API connection...")
    print("-" * 50)
    
    try:
        # Initialize Groq client
        client = Groq(api_key=api_key)
        
        # Make a simple test request
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": "Say 'Hello, Groq API is working!' in a friendly way."
                }
            ],
            temperature=0.7,
            max_tokens=100
        )
        
        # Get the response
        result = response.choices[0].message.content
        
        print("✅ SUCCESS! Groq API is working!")
        print("-" * 50)
        print(f"Response: {result}")
        print("-" * 50)
        print(f"Model used: {response.model}")
        print(f"Tokens used: {response.usage.total_tokens}")
        
        return True
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

if __name__ == "__main__":
    print("="*50)
    print("🧪 GROQ API KEY TESTER")
    print("="*50)
    
    success = test_groq_api()
    
    if success:
        print("\n✅ Your Groq API key is working perfectly!")
        print("You can now run your main application.")
    else:
        print("\n❌ Groq API test failed!")
        print("Please check:")
        print("1. Your .env file has GROQ_API_KEY")
        print("2. The API key is correct")
        print("3. You have internet connection")
