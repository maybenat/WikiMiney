class CreateClusters < ActiveRecord::Migration
  def change
    create_table :clusters do |t|
      t.string :project
      t.string :page
      t.string :year
      t.string :month
      t.integer :views, :limit => 8
      t.integer :bytes, :limit => 8
      t.string :cluster, presence: true
      t.timestamps
    end
  end
end
