import mysql.connector
import cv2
import os

# Function to connect to MySQL
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='pothole_detection'
        )
        print("Connected to the database successfully!")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None


# Function to store images in the database
def store_images(conn, image_paths):
    try:
        cursor = conn.cursor()
        for image_path in image_paths:
            # Check if the image file exists
            if not os.path.isfile(image_path):
                print(f"Image file not found: {image_path}")
                continue  # Skip if the file doesn't exist

            with open(image_path, 'rb') as file:
                binary_image = file.read()
            sql = "INSERT INTO detections (image) VALUES (%s)"
            cursor.execute(sql, (binary_image,))
            print(f"Stored image: {image_path}")  # Print confirmation for each stored image
        conn.commit()
        print("All images stored successfully!")  # Confirmation for all images
    except Exception as e:
        print(f"Error storing images: {e}")
    finally:
        cursor.close()


# Function to retrieve and save images from the database
def retrieve_images(conn):
    try:
        cursor = conn.cursor()
        sql = "SELECT image FROM detections"
        cursor.execute(sql)
        results = cursor.fetchall()

        # Create a directory to save retrieved images if it doesn't exist
        os.makedirs("retrieved_images", exist_ok=True)

        if results:
            for i, row in enumerate(results):
                image_data = row[0]  # Get binary image data
                image_path = f"retrieved_images/retrieved_image_{i}.jpg"

                # Save image to file
                with open(image_path, 'wb') as file:
                    file.write(image_data)

                # Print confirmation for each image
                print(f"Image {i} saved as {image_path}")

                # Load and display the image using OpenCV
                img = cv2.imread(image_path)
                if img is not None:
                    cv2.imshow(f"Image {i}", img)
                    cv2.waitKey(0)  # Wait for a key press
                    cv2.destroyAllWindows()  # Release resources after displaying
                else:
                    print(f"Error loading image {i} from {image_path}. The file might be corrupted.")
            print("All images retrieved and saved successfully!")  # Final confirmation
        else:
            print("No images found in the database.")

    except Exception as e:
        print(f"Error retrieving images: {e}")
    finally:
        cursor.close()


# Main function to connect, store, and retrieve images
def main():
    conn = connect_to_database()
    if conn:
        # Store images in the database
        image_paths = [
            "C:/Users/HP/Downloads/index4.jpg",
            "C:/Users/HP/Downloads/index2.jpg"
        ]
        store_images(conn, image_paths)

        # Retrieve images from the database
        retrieve_images(conn)
        conn.close()


if __name__ == "__main__":
    main()
