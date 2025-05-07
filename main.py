from Hotel_reviews import Data_processing,word_cloud, geo_module


def main():
    print("🚀 Starting full hotel reviews analysis pipeline...")

    # Step 1: Data processing
    print("📥 Step 1: Loading and preparing data...")
    df = Data_processing.load_and_prepare_data("tripadvisor_hotel_reviews.csv")
    df.to_csv("tripadvisor_reviews_ready.csv", index=False)
    print("✅ Data saved to 'tripadvisor_reviews_ready.csv'.")

    # Step 2: Word cloud generation
    print("☁️ Step 2: Generating word clouds...")
    word_cloud.create_wordclouds(df)
    print("✅ Word clouds saved in 'Hotel_reviews/output/'.")

    # Step 3: Add random city info
    print("🌍 Step 3: Adding city information...")
    df_with_city = geo_module.add_random_city(df)
    df_with_city.to_csv("tripadvisor_reviews_with_city.csv", index=False)
    print("✅ Data with cities saved to 'tripadvisor_reviews_with_city.csv'.")

    print("\n🎉 Done! All files are ready for Power BI visualization.")

if __name__ == "__main__":
    main()
