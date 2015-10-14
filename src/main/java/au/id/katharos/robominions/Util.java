package au.id.katharos.robominions;

import java.util.HashMap;

import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.World;
import org.bukkit.entity.EntityType;

import au.id.katharos.robominions.api.Materials;
import au.id.katharos.robominions.api.Materials.Material.Type;
import au.id.katharos.robominions.api.RobotApi.Coordinate;
import au.id.katharos.robominions.api.RobotApi.RoboEntityType;
import au.id.katharos.robominions.api.RobotApi.RoboEntityType.RoboEntityTypeEnum;

import com.google.common.collect.Maps;

/**
 * Class for static utility methods.
 */
public class Util {

	public static final HashMap<EntityType, RoboEntityTypeEnum> entityTypeMap = Maps.newHashMap();
	
	static {
		entityTypeMap.put(EntityType.CHICKEN, RoboEntityTypeEnum.CHICKEN);
		entityTypeMap.put(EntityType.COW, RoboEntityTypeEnum.COW);
		entityTypeMap.put(EntityType.HORSE, RoboEntityTypeEnum.HORSE);
		entityTypeMap.put(EntityType.OCELOT, RoboEntityTypeEnum.OCELOT);
		entityTypeMap.put(EntityType.PIG, RoboEntityTypeEnum.PIG);
		entityTypeMap.put(EntityType.RABBIT, RoboEntityTypeEnum.RABBIT);
		entityTypeMap.put(EntityType.SHEEP, RoboEntityTypeEnum.SHEEP);
		entityTypeMap.put(EntityType.WOLF, RoboEntityTypeEnum.WOLF);
		entityTypeMap.put(EntityType.VILLAGER, RoboEntityTypeEnum.VILLAGER);
		entityTypeMap.put(EntityType.IRON_GOLEM, RoboEntityTypeEnum.IRON_GOLEM);
		entityTypeMap.put(EntityType.SNOWMAN, RoboEntityTypeEnum.SNOWMAN);
		entityTypeMap.put(EntityType.BLAZE, RoboEntityTypeEnum.BLAZE);
		entityTypeMap.put(EntityType.CREEPER, RoboEntityTypeEnum.CREEPER);
		entityTypeMap.put(EntityType.ENDERMAN, RoboEntityTypeEnum.ENDERMAN);
		entityTypeMap.put(EntityType.ENDERMITE, RoboEntityTypeEnum.ENDERMITE);
		entityTypeMap.put(EntityType.GIANT, RoboEntityTypeEnum.GIANT);
		entityTypeMap.put(EntityType.GUARDIAN, RoboEntityTypeEnum.GUARDIAN);
		entityTypeMap.put(EntityType.SILVERFISH, RoboEntityTypeEnum.SILVERFISH);
		entityTypeMap.put(EntityType.SKELETON, RoboEntityTypeEnum.SKELETON);
		entityTypeMap.put(EntityType.SPIDER, RoboEntityTypeEnum.SPIDER);
		entityTypeMap.put(EntityType.WITCH, RoboEntityTypeEnum.WITCH);
		entityTypeMap.put(EntityType.WITHER, RoboEntityTypeEnum.WITHER);
		entityTypeMap.put(EntityType.ZOMBIE, RoboEntityTypeEnum.ZOMBIE);	
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
		RoboEntityTypeEnum roboEntTypeEnum;
		if (entityTypeMap.containsKey(type)) {
			roboEntTypeEnum = entityTypeMap.get(type);
		} else {
			roboEntTypeEnum = RoboEntityTypeEnum.UNRECOGNIZED;
		}
		return RoboEntityType.newBuilder().setType(roboEntTypeEnum).build();
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
