class CreateWikis < ActiveRecord::Migration
  def change
    create_table :wikipages do |t|
      t.string :project
      t.string :page
      t.timestamps
    end

    create_table :wikiviews do |t|
      t.belongs_to :wikipage, index: true
      t.string :year
      t.string :month
      t.string :day
      t.integer :views, :limit => 8
      t.integer :bytes, :limit => 8
      t.timestamps
    end
  end
end
