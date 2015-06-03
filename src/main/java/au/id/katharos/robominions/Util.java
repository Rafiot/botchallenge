package au.id.katharos.robominions;

import java.util.HashMap;

import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.World;
import org.bukkit.entity.EntityType;

import au.id.katharos.robominions.api.Materials;
import au.id.katharos.robominions.api.Materials.Material.Type;
import au.id.katharos.robominions.api.RobotApi.Coordinate;
import au.id.katharos.robominions.api.RobotApi.RoboEntity.RoboEntityType;

import com.google.common.collect.Maps;

/**
 * Class for static utility methods.
 */
public class Util {

	public static final HashMap<EntityType, RoboEntityType> entityTypeMap = Maps.newHashMap();
	
	static {
		entityTypeMap.put(EntityType.CHICKEN, RoboEntityType.CHICKEN);
		entityTypeMap.put(EntityType.COW, RoboEntityType.COW);
		entityTypeMap.put(EntityType.HORSE, RoboEntityType.HORSE);
		entityTypeMap.put(EntityType.OCELOT, RoboEntityType.OCELOT);
		entityTypeMap.put(EntityType.PIG, RoboEntityType.PIG);
		entityTypeMap.put(EntityType.RABBIT, RoboEntityType.RABBIT);
		entityTypeMap.put(EntityType.SHEEP, RoboEntityType.SHEEP);
		entityTypeMap.put(EntityType.WOLF, RoboEntityType.WOLF);
		entityTypeMap.put(EntityType.VILLAGER, RoboEntityType.VILLAGER);
		entityTypeMap.put(EntityType.IRON_GOLEM, RoboEntityType.IRON_GOLEM);
		entityTypeMap.put(EntityType.SNOWMAN, RoboEntityType.SNOWMAN);
		entityTypeMap.put(EntityType.BLAZE, RoboEntityType.BLAZE);
		entityTypeMap.put(EntityType.CREEPER, RoboEntityType.CREEPER);
		entityTypeMap.put(EntityType.ENDERMAN, RoboEntityType.ENDERMAN);
		entityTypeMap.put(EntityType.ENDERMITE, RoboEntityType.ENDERMITE);
		entityTypeMap.put(EntityType.GIANT, RoboEntityType.GIANT);
		entityTypeMap.put(EntityType.GUARDIAN, RoboEntityType.GUARDIAN);
		entityTypeMap.put(EntityType.SILVERFISH, RoboEntityType.SILVERFISH);
		entityTypeMap.put(EntityType.SKELETON, RoboEntityType.SKELETON);
		entityTypeMap.put(EntityType.SPIDER, RoboEntityType.SPIDER);
		entityTypeMap.put(EntityType.WITCH, RoboEntityType.WITCH);
		entityTypeMap.put(EntityType.WITHER, RoboEntityType.WITHER);
		entityTypeMap.put(EntityType.ZOMBIE, RoboEntityType.ZOMBIE);	
	}

	public static Location locationFromCoords(World world, Coordinate coords) {
		return new Location(world, coords.getX(), coords.getY(), coords.getZ());
	}
	
	public static boolean materialsEqual(Material a, Material b) {
		// Special case, LOG and LOG_2 are equivalent
		if (a == Material.LOG || a == Material.LOG_2) {
			return b == Material.LOG || b == Material.LOG_2;
		} 
		return a == b;
	}
	
	public static Coordinate coordsFromLocation(Location location) {
		return Coordinate.newBuilder()
				.setX(location.getBlockX())
				.setY(location.getBlockY())
				.setZ(location.getBlockZ())
				.build();
	}

	public static RoboEntityType roboEntityTypeFromEntityType(EntityType type) {
		if (entityTypeMap.containsKey(type)) {
			return entityTypeMap.get(type);
		} else {
			return RoboEntityType.UNRECOGNIZED;
		}
	}
	
	public static Materials.Material toProtoMaterial(Material material) {
		return toProtoMaterial(material, false);
	}
	
	@SuppressWarnings("deprecation") // No alternative
	public static Materials.Material toProtoMaterial(Material material, boolean exact) {
		if (!exact && material == Material.LOG_2) {
			material = Material.LOG;
		}
		Materials.Material protoMaterial = Materials.Material.newBuilder()
				.setType(Type.valueOf(material.getId())).build();
		return protoMaterial;
	}

	@SuppressWarnings("deprecation") // No alternative
	public static Material toBukkitMaterial(Materials.Material protoMaterial) {
		return Material.getMaterial(protoMaterial.getType().getNumber());
	}
}
