class CreateWikis < ActiveRecord::Migration
  def change
    create_table :wikis do |t|
      t.string :project
      t.string :page
      t.integer :views, :limit => 8
      t.integer :bytes, :limit => 8

      t.timestamps
    end
  end
end
